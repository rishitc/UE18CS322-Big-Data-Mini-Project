import time  # For timestamps
import os  # Needed to test reference to YACS Protocol for createMessageToMaster()
import json  # For working on JSON data
import threading
import socket

from Communication.protocol import YACS_Protocol

class Worker:
    """
    - This Class simulates the worker through following steps:
        1. It gets YACS Protocol Message (created using the
            ***createMessageToWorker()***) from the Master
        1. It adds the particular task to its execution pool.
            - **NOTE:** (Assumption? based on scheduling algorithm)
            - The worker will not be handed any task when its execution pool is
            full
        1. Run (i.e. simulate) the tasks by decrementing the *remaining_time*
            value each second
        1. Once a particular task finishes execution, the worker removes it
            from the execution pool and sends a message back to the Master
            using YACS Protocol Message (***createMessageToMaster()***)
    """
    def __init__(self, WorkerID):  # Still need to add depending on specs
        self.tasks = dict()  
        self.ID = WorkerID
        self.LOCK = threading.Lock()
        self.updates_q = queue.Queue()

    def listenForTaskRequest(self, taskRequestSocket: socket.socket):
        """
        This listens for a JSON message which was created using the
        ***createMessageToWorker()*** method (*i.e. following the set protocol
        format*) and then sets its key for the particular instance of worker as task id
        and the value is all the related information of the task, i.e the dictionary obtained
        from **createMessageToWorker()** method.
        """
        while True:
            # To extract the message sent
            taskRequest = taskRequestSocket.recv(MESSAGE_BUFFER_SIZE).decode()
            if not taskRequest:
                taskRequestSocket.close()
                break
            
            # Convert JSON to python dictionary
            python_protocol_message = json.loads(taskRequest)

            # To obtain key for addition to exec poll(i.e tasks)
            job_in_message = python_protocol_message["job_id"]
            task_in_message = python_protocol_message["task"]["task_id"]

            python_protocol_message["task"]["start time"] = time.time() # Store the starting time of the task
            python_protocol_message["task"]["end time"] = 0

            self.LOCK.acquire()
            self.tasks[job_in_message][task_in_message] = python_protocol_message #Value for the tasks dictionary will be all the info
            self.LOCK.release()
        # passed from the Master along with the necessary time stamps added above

    def simulateWorker(self):
        # While there is a task to execute in the task-pool
        while True:
            # Get the number of tasks in the Task pool
            self.LOCK.acquire()
            tasksInExecutionPool_Count = len(self.tasks)
            self.LOCK.release()

            # If there are tasks to execute in the task pool
            if tasksInExecutionPool_Count != 0:
                self.LOCK.acquire()
                for job_id in self.tasks:
                """Durations (i.e. the value in the dictionary) will be
                   positive(non-zero) integers."""
                    for task_id in job_id:
                    # Reduce the duration of the task by 1
                        self.tasks[job_id][task_id]["task"]["duration"] -= 1

                # Check if the duration has become 0, i.e. the task has
                # finished execution
                        if self.tasks[job_id][task_id]["task"]["duration"] == 0:
                            self.tasks[job_id][task_id]["task"]["end time"] = time.time() # Store the end-time of the task
                            response_message_to_master=YACS_Protocol\
                                .createMessageToMaster(self.tasks[job_id][task_id]["job_id"],
                                                       self.tasks[job_id][task_id]["task family"],
                                                       self.tasks[job_id][task_id]["task"]["task_id"],
                                                       self.tasks[job_id][task_id]["task"]["start time"],
                                                       self.tasks[job_id][task_id]["task"]["end time"],
                                                       self.tasks[job_id][task_id]["worker_id"])
                            self.update_q.put(response_message_to_master)
                            del self.tasks[job_id][task_id] # Remove the task entry from the execution pool
                            if len(self.tasks[job_id]==0):  # Remove the job entry if there are no tasks of that particular job
                                del self.tasks[job_id]
                # Sleeps for 1 second until next check on the values
                    self.LOCK.release()
                    time.sleep(1)
        # NOTE: Need to add the portion wherein the worker needs to listen
        # for messages if dict is empty
        # NOTE: Need to first establish communication between master and
        # worker for that
        # UPDATE: Acknowledged. Working on that right now. 

    def taskComplete(self, reply_socket: socket.socket):
        """
        This method creates and returns returns the **JSON string**
        of format createMessageToMaster() of YACS Protocol.

        This method is called by ***simulateWorker()*** method when the
        *remaining_duration attribute* of the task **becomes 0**.
        """   

        while True:
            if not self.update_q.empty():
                response_msg: str = self.update_q.get()
                self.update_q.task_done()
                # send it
                reply_socket.sendall(response_msg.encode())
