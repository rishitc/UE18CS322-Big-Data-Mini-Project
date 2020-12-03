import time  # For times
import json  # For JSON to python conversion and vice-versa
import threading  # For locks
import socket  # For function parameters
import queue  # For storing the completed tasks
from cryptography.fernet import Fernet
import colored as TC

from Locks.WorkerPrintLock import worker
from Communication.protocol import YACS_Protocol
# from master import PRINT_LOCK
#  For sending message back to master

MESSAGE_BUFFER_SIZE = 4096  # Socket receiving length


class Worker:
    """
    - This Class simulates the worker through following steps:
        1. It gets YACS Protocol Message (created using the
            ***createMessageToWorker()***) from the Master.
        1. It adds the particular task to its execution pool.
            - The worker will not be handed any task when its execution pool is
            full.
        1. Run (i.e. simulate) the tasks by decrementing the *remaining_time*
            value each second.
        1. Once a particular task finishes execution, the worker removes it
            from the execution pool and sends a message back to the Master
            using YACS Protocol Message (***createMessageToMaster()***).
    """
    def __init__(self, WorkerID):
        self.tasks = dict()  # Task Execution Pool
        self.ID = WorkerID  # Unique Worker ID
        self.LOCK = threading.Lock()
        self.updates_q = queue.Queue()  # For completed tasks

    def listenForTaskRequest(self, taskRequestSocket: socket.socket,
                             WORKER_KEY):
        """
        This listens for a JSON message which was created using the
        ***createMessageToWorker()*** method (*i.e. following the set protocol
        format*) and then sets its key for the particular instance of worker
        as task id and the value is all the related information of the task,
        i.e the dictionary obtained from **createMessageToWorker()** method.
        """
        dec_obj = Fernet(WORKER_KEY)
        # Fernet uses a key for symmetric encryption/decryption

        # Thread to log when the worker task pool is empty
        _exec_pool_poller_thread = threading\
            .Thread(name="Task Pool Poller Thread",
                    target=self.tasksPoolPoller)
        _exec_pool_poller_thread.daemon = True
        _exec_pool_poller_thread.start()
        worker.PRINT_LOCK.acquire()
        print(Worker.info_text("Created the Task Execution Pool Poller thread!"
                               ))
        worker.PRINT_LOCK.release()

        while True:
            # To extract the message sent from master
            taskRequest = taskRequestSocket.recv(MESSAGE_BUFFER_SIZE).decode()
            if not taskRequest:
                taskRequestSocket.close()
                break

            _temp: str = ''
            for i in taskRequest.split('==')[:-1]:
                _temp += dec_obj.decrypt((i + '==').encode()).decode()
            taskRequest = _temp

            # Preprocess the received JSON data. This helps prevent
            # JSON parsing errors when more then one message has been
            # received at once at the worker
            taskRequest = "[" + taskRequest.replace("}{", "},{") + "]"

            # For logging purposes
            worker.PRINT_LOCK.acquire()
            print(f"Task received at worker: {taskRequest}")
            worker.PRINT_LOCK.release()

            # Convert JSON to python dictionary
            python_protocol_message = json.loads(taskRequest)

            # Acquiring lock as shared object is accessed
            self.LOCK.acquire()

            # request: messageToWorker type
            for request in python_protocol_message:
                # To obtain key for addition to task exec pool
                job_in_message = request["job_id"]
                task_in_message = request["task"]["task_id"]
                # Initialise the starting time of the task
                request["task"]["start_time"] = time.time()
                request["task"]["end_time"] = 0
                # Adding components that are there in reply message to the
                # master but not in the received message
                worker.PRINT_LOCK.acquire()
                print(request)
                worker.PRINT_LOCK.release()
                if self.tasks.get(job_in_message) is None:
                    self.tasks[job_in_message] = dict()
                # The dictionary that stores the incoming task requests is a
                # nested dictionary with first level key as job_id and the
                # value being another dictionary with task_id(unique for a job)
                # as the key for this nested dictionary and value being the
                # actual response to the master

                self.tasks[job_in_message][task_in_message] = request

            self.LOCK.release()  # Release lock as CS code is complete

            worker.PRINT_LOCK.acquire()
            print(self.tasks)  # Print the task exec pool
            worker.PRINT_LOCK.release()

        _exec_pool_poller_thread.join()

    def simulateWorker(self):
        # While there is a task to execute in the task exec pool
        while True:
            # Get the number of tasks in the Task pool
            self.LOCK.acquire()  # Acquiring lock as shared object is accessed
            tasksInExecutionPool_Count = len(self.tasks)  # Returns no_of_jobs
            self.LOCK.release()  # Release lock as CS code is complete

            # If there are tasks to execute in the task pool
            if tasksInExecutionPool_Count != 0:
                self.LOCK.acquire()  # Lock as shared object is accessed
                _temp_1 = list(self.tasks)  # Need to store as list for
                for job_id in _temp_1:      # correct iterating
                    """Durations (i.e. the value in the dictionary) will be
                    positive(non-zero) integers."""
                    _temp_2 = list(self.tasks[job_id])
                    for task_id in _temp_2:
                        # Reduce the duration of the task by 1
                        worker.PRINT_LOCK.acquire()
                        print(type(self.tasks[job_id][task_id]["task"]
                                   ["duration"]))
                        print(self.tasks[job_id][task_id]["task"]["duration"])
                        worker.PRINT_LOCK.release()
                        self.tasks[job_id][task_id]["task"]["duration"] -= 1

                        # Check if the duration has become 0, i.e. the task has
                        # finished execution
                        if (self.tasks[job_id][task_id]["task"]["duration"]
                                == 0):
                            self.tasks[job_id][task_id]["task"]["end_time"] = \
                                time.time()
                            # Store the end-time of the task
                            response_message_to_master = YACS_Protocol\
                                .createMessageToMaster((self.tasks[job_id]
                                                        [task_id]["job_id"]),
                                                       (self.tasks[job_id]
                                                        [task_id]
                                                        ["task_family"]),
                                                       (self.tasks[job_id]
                                                        [task_id]["task"]
                                                        ["task_id"]),
                                                       (self.tasks[job_id]
                                                        [task_id]["task"]
                                                        ["start_time"]),
                                                       (self.tasks[job_id]
                                                        [task_id]["task"]
                                                        ["end_time"]),
                                                       (self.tasks[job_id]
                                                        [task_id]
                                                        ["worker_id"]))
                            # YACS Protocol based response to master
                            self.updates_q.put(response_message_to_master)
                            # Adding the task in the completed tasks queue
                            # The queue is a shared object that can be accessed
                            # between separate threads
                            del self.tasks[job_id][task_id]
                            # Remove the task entry from the task exec pool
                            if len(self.tasks[job_id]) == 0:
                                del self.tasks[job_id]
                            # Remove the job entry if there are no tasks of
                            # that particular job
                # Sleeps for 1 second until next check on the values
                self.LOCK.release()  # Release lock as CS code is complete
                time.sleep(1)
        # NOTE: Need to add the portion wherein the worker needs to listen
        # for messages if dict is empty
        # UPDATE: Taken care of by the forever loop
        # NOTE: Need to first establish communication between master and
        # worker for that
        # UPDATE 1: Acknowledged. Working on that right now.
        # UPDATE 2: The same has been implemented

    def taskComplete(self, reply_socket: socket.socket, WORKER_KEY):
        """
        This method creates and returns returns the **JSON string**
        of format createMessageToMaster() of YACS Protocol.

        This method is called by ***simulateWorker()*** method when the
        *remaining_duration attribute* of the task **becomes 0**.
        """
        enc_obj = Fernet(WORKER_KEY)
        while True:
            if not self.updates_q.empty():
                response_msg: str = self.updates_q.get()
                self.updates_q.task_done()
                # get() and task_done() are similar to lock()
                # and release() for the queue
                # Sending to master
                reply_socket.sendall(enc_obj.encrypt(response_msg.encode()))
                worker.PRINT_LOCK.acquire()
                print(f"Task sent: {response_msg}!")
                worker.PRINT_LOCK.release()
                # time.sleep(0.01)

    @staticmethod
    def info_text(text):
        """```info_text``` returns a modified version of the input ```text``` such
        that it looks like an *information message* when printed on the CLI.

        **param** ```text```: The input string that will be modified to look
        like an *information message* when printed on the CLI

        **type** ```text```: str

        **return**: The modified version of the input ```text``` such
        that it looks like an *information message* when printed on the CLI

        **rtype**: str
        """
        return f"{TC.fg(6) + TC.attr(1)}INFO:{TC.attr(0)} {text}"

    def tasksPoolPoller(self):
        isTaskPoolEmpty: bool = False
        wasTaskPoolEmpty: bool = False
        # Prints when the task pool is empty
        while True:
            self.LOCK.acquire()
            isTaskPoolEmpty = not self.tasks
            self.LOCK.release()

            if isTaskPoolEmpty and not wasTaskPoolEmpty:
                worker.PRINT_LOCK.acquire()
                print(Worker.info_text("The task execution pool is empty!")
                      )
                worker.PRINT_LOCK.release()

            wasTaskPoolEmpty = isTaskPoolEmpty

    def __del__(self):
        self.updates_q.join()  # block until all tasks are done
