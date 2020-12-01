import time  # For times
import json  # For JSON to python conversion and vice-versa
import threading  # For locks
import socket  # For function parameters
import queue  # For storing the completed tasks

from Communication.protocol import YACS_Protocol
#  For sending message back to master

MESSAGE_BUFFER_SIZE = 4096  # Socket receiving length


class Worker:
    """
    - This Class simulates the worker through following steps:
        1. It gets YACS Protocol Message (created using the
            ***createMessageToWorker()***) from the Master
        1. It adds the particular task to its execution pool.
            - The worker will not be handed any task when its execution pool is
            full
        1. Run (i.e. simulate) the tasks by decrementing the *remaining_time*
            value each second
        1. Once a particular task finishes execution, the worker removes it
            from the execution pool and sends a message back to the Master
            using YACS Protocol Message (***createMessageToMaster()***)
    """
    def __init__(self, WorkerID):
        self.tasks = dict()  # Task Execution Pool
        self.ID = WorkerID  # Unique Worker ID
        self.LOCK = threading.Lock()
        self.updates_q = queue.Queue()  # For completed tasks

    def listenForTaskRequest(self, taskRequestSocket: socket.socket):
        """
        This listens for a JSON message which was created using the
        ***createMessageToWorker()*** method (*i.e. following the set protocol
        format*) and then sets its key for the particular instance of worker
        as task id and the value is all the related information of the task,
        i.e the dictionary obtained from **createMessageToWorker()** method.
        """
        while True:
            # To extract the message sent from master
            taskRequest = taskRequestSocket.recv(MESSAGE_BUFFER_SIZE).decode()
            if not taskRequest:
                taskRequestSocket.close()
                break
            # Convert JSON to python dictionary
            python_protocol_message = json.loads(taskRequest)

            # To obtain key for addition to task exec pool
            job_in_message = python_protocol_message["job_id"]
            task_in_message = python_protocol_message["task"]["task_id"]
            # Initialise the starting time of the task
            python_protocol_message["task"]["start time"] = time.time()
            python_protocol_message["task"]["end time"] = 0
            # Adding components that are there in reply message to the master
            # but not in the received message

            self.LOCK.acquire()  # Acquiring lock as shared object is accessed
            self.tasks[job_in_message][task_in_message] = \
                python_protocol_message
            #  Value for the tasks dictionary will be all the info
            self.LOCK.release()  # Release lock as CS code is complete

    def simulateWorker(self):
        # While there is a task to execute in the task exec pool
        while True:
            # Get the number of tasks in the Task pool
            self.LOCK.acquire()  # Acquiring lock as shared object is accessed
            tasksInExecutionPool_Count = len(self.tasks)
            self.LOCK.release()  # Release lock as CS code is complete

            # If there are tasks to execute in the task pool
            if tasksInExecutionPool_Count != 0:
                self.LOCK.acquire()  # Lock as shared object is accessed
                for job_id in self.tasks:
                    """Durations (i.e. the value in the dictionary) will be
                    positive(non-zero) integers."""
                    for task_id in job_id:
                        # Reduce the duration of the task by 1
                        self.tasks[job_id][task_id]["task"]["duration"] -= 1

                # Check if the duration has become 0, i.e. the task has
                # finished execution
                        if (self.tasks[job_id][task_id]["task"]["duration"]
                                == 0):
                            self.tasks[job_id][task_id]["task"]["end time"] = \
                                time.time()
                            # Store the end-time of the task
                            response_message_to_master = YACS_Protocol\
                                .createMessageToMaster((self.tasks[job_id]
                                                        [task_id]["job_id"]),
                                                       (self.tasks[job_id]
                                                        [task_id]
                                                        ["task family"]),
                                                       (self.tasks[job_id]
                                                        [task_id]["task"]
                                                        ["task_id"]),
                                                       (self.tasks[job_id]
                                                        [task_id]["task"]
                                                        ["start time"]),
                                                       (self.tasks[job_id]
                                                        [task_id]["task"]
                                                        ["end time"]),
                                                       (self.tasks[job_id]
                                                        [task_id]
                                                        ["worker_id"]))
                            # YACS Protocol based response to master
                            self.updates_q.put(response_message_to_master)
                            # Adding the task in the completed tasks queue
                            del self.tasks[job_id][task_id]
                            # Remove the task entry from the task exec pool
                            if len(self.tasks[job_id] == 0):
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

    def taskComplete(self, reply_socket: socket.socket):
        """
        This method creates and returns returns the **JSON string**
        of format createMessageToMaster() of YACS Protocol.

        This method is called by ***simulateWorker()*** method when the
        *remaining_duration attribute* of the task **becomes 0**.
        """

        while True:
            if not self.updates_q.empty():
                response_msg: str = self.updates_q.get()
                self.updates_q.task_done()
                # Sending to master
                reply_socket.sendall(response_msg.encode())
