import time  # For timestamps
import os  # Needed to test reference to YACS Protocol for createMessageToMaster()
import json  # For working on JSON data
import threading
from threading import Lock
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
        self.tasks = dict()  # Task ID as key and duration as value
        self.ID = WorkerID
        self.LOCK = Lock() 

    def listenForTask(self,worker_instance,json_protcol_message):
        """
        This listens for a JSON message which was created using the
        ***createMessageToWorker()*** method (*i.e. following the set protocol
        format*) and then sets its key for the particular instance of worker as task id
        and the value is all the related information of the task, i.e the dictionary obtained
        from **createMessageToWorker()** method.
        """
        # Convert JSON to python dictionary
        python_protocol_message = json.loads(json_protcol_message)

        # To obtain key for addition to exec poll(i.e tasks)
        self.job_in_message = python_protocol_message["job_id"]
        self.task_in_message = python_protocol_message["task"]["task_id"]
        
        python_protocol_message["task"]["start time"] = time.time() # Store the starting time of the task
        python_protocol_message["task"]["end time"] = 0
        python_protocol_message["task"]["task turnaround time"] = 0
        self.tasks[self.job_in_message][self.task_in_message] = python_protocol_message #Value for the tasks dictionary will be all the info
        # passed from the Master along with the necessary time stamps added above

    def simulateWorker(self):
        # While there is a task to execute in the task-pool
        while len(self.tasks) != 0:
            for task_id in self.tasks:
                """Durations (i.e. the value in the dictionary) will be
                   positive(non-zero) integers."""

                # Reduce the duration of the task by 1
                self.tasks[task_id]["task"]["duration"] -= 1

                # Check if the duration has become 0, i.e. the task has
                # finished execution
                if self.tasks[task_id]["task"]["duration"] == 0:
                    self.tasks[task_id]["task"]["end time"]=time.time() # Store the end-time of the task
                    return self.taskComplete(self.tasks[task_id])

                # NOTE: Below is the older version of the code,
                # What is seen above is the proposed replacement
                #
                # if self.tasks[task_id] != 0:
                #     # Reduce the duration of the task by 1
                #     self.tasks[task_id] -= 1
                # else:
                #     self.taskComplete(self.tasks[task_id])

            # Sleeps for 1 second until next check on the values
            time.sleep(1)
        # NOTE: Need to add the portion wherein the worker needs to listen
        # for messages if dict is empty
        # NOTE: Need to first establish communication between master and
        # worker for that
        # UPDATE: Acknowledged. Working on that right now. 

    def taskComplete(self, task_id):
        """
        This method creates and returns returns the **JSON string**
        of format createMessageToMaster() of YACS Protocol.

        This method is called by ***simulateWorker()*** method when the
        *remaining_duration attribute* of the task **becomes 0**.
        """
        
        # Give by: (waiting_time + cpu_burst_time), i.e. (end - start) in
        # this context
        self.tasks[task_id]["task"]["task turnaround time"]= self.tasks[task_id]["task"]["end time"] - self.[task_id]["task"]["start time"]

        # Can also call the YACS Protocol class's createMessageToMaster() for
        # this

        # Calling the createMessageToMaster method of YACS_Protocol Class
        response_message_to_master=YACS_Protocol.createMessageToMaster(self.tasks[task_id]["job_id"],self.tasks[task_id]["task family"],self.tasks[task_id]["task"]["task_id"],
                                                                       self.tasks[task_id]["task"]["start time"],self.tasks[task_id]["task"]["end time"],
                                                                       self.tasks[task_id]["worker_id"],self.tasks[task_id]["task"]["task turnaround time"])
        # Python dictionary for response message in case YACS_Protocol function is not called
        """response_message_to_master = dict()
        response_message_to_master["worker_id"]=self.workerID_in_message
        response_message_to_master["job_id"]=self.jobID_in_message
        response_message_to_master["task family"]=self.taskfamily_in_message
        response_message_to_master["task"]={}
        response_message_to_master["task"]["task_id"]=self.task_in_message
        response_message_to_master["task"]["start time"]=self.startTime
        response_message_to_master["task"]["end time"]=self.endTime
        response_message_to_master["task"]["task turnaround time"]=self.turnoverTime
        response_message_to_master["task"]["duration"]=self.duration_in_message"""

        # Remove the task entry from the execution pool
        del self.tasks[task_id]

        # Return the JSON string to the master
        return json.dumps(response_message_to_master)
