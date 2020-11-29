import time  # For timestamps
import os  # Needed to test reference to YACS Protocol for createMessageToMaster()
import json  # For working on JSON data
from threading import Lock


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
    def __init__(self, WorkerTaskPool):  # Still need to add depending on specs
        self.tasks = dict()  # Task ID as key and duration as value
        self.taskpool = WorkerTaskPool
        self.LOCK = Lock()  # Where to use??
        self.startTime = 0
        self.endTime = 0
        self.turnoverTime = 0

    def listenForTask(self, json_protcol_message):
        """
        This listens for a ***createMessageToWorker()*** message and the sets
        initial variables as per the incoming JSON message.
        """
        # Convert JSON to python dictionary
        python_protocol_message = json.loads(json_protcol_message)

        # The below 2 values are essential for the simulation or worker
        # computation
        self.task_in_message = python_protocol_message["task"][0]["task_id"]
        self.duration_in_message = (python_protocol_message["task"][0]
                                    ["duration"])

        # The below variables are essential for the createMessageToMaster()
        # YACS Protocol once the task completes execution
        self.workerID_in_message = python_protocol_message["worker_id"]
        self.jobID_in_message = python_protocol_message["job_id"]
        self.taskfamily_in_message = python_protocol_message["task family"]

        # Key-Value pair (both integers) with task id as key and initial
        # duration as value
        self.tasks[self.task_in_message] = self.duration_in_message
        self.startTime = time.time()  # Store the starting time of the task

    def simulateWorker(self):
        # While there is a task to execute in the task-pool
        while len(self.tasks) != 0:
            for task_id in self.tasks:
                """Durations (i.e. the value in the dictionary) will be
                   positive(non-zero) integers."""

                # Reduce the duration of the task by 1
                self.tasks[task_id] -= 1

                # Check if the duration has become 0, i.e. the task has
                # finished execution
                if self.tasks[task_id] == 0:
                    self.taskComplete(self.tasks[task_id])

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
        # worker for that for that

    def taskComplete(self, task_id):
        """
        This method creates and returns returns the **JSON string**
        of format createMessageToMaster() of YACS Protocol.

        This method is called by ***simulateWorker()*** method when the
        *remaining_duration attribute* of the task **becomes 0**.
        """
        self.endTime = time.time()  # Store the end-time of the task

        # Give by: (waiting_time + cpu_burst_time), i.e. (end - start) in
        # this context
        self.turnoverTime = self.endTime - self.startTime

        # Can also call the YACS Protocol class's createMessageToWorker() for
        # this
        # NOTE: You should call YACS Protocol class's createMessageToMaster()
        #       for this! and not createMessageToWorker()

        # Python dictionary for response message
        response_message_to_master = dict()
        response_message_to_master["worker_id"]=self.workerID_in_message
        response_message_to_master["job_id"]=self.jobID_in_message
        response_message_to_master["task family"]=self.taskfamily_in_message
        response_message_to_master["task"]={}
        response_message_to_master["task"]["task_id"]=self.task_in_message
        response_message_to_master["task"]["start time"]=self.startTime
        response_message_to_master["task"]["end time"]=self.endTime
        response_message_to_master["task"]["task turnaround time"]=self.turnoverTime
        response_message_to_master["task"]["duration"]=self.duration_in_message

        # Remove the task entry from the execution pool
        del self.tasks[task_id]

        # Return the JSON string to the master
        return json.dumps(response_message_to_master)
