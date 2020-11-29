import time  # For timestamps
import os  # Needed to test reference to YACS Protocol for createMessageToMaster()
import json  # For working on JSON data
from threading import Lock


class Worker:
    """
    - This Class simulates the worker through following steps:
        1. It gets YACS Protocol Message (created using the
            ***CreateMessageToWorker()***) from the Master
        1. It adds the particular task to its execution pool.
            - **NOTE:** (Assumption? based on scheduling algorithm)
            - The worker will not be handed any task when its execution pool is
            full
        1. Run (i.e. simulate) the tasks by decrementing the *remaining_time*
            value each second
        1. Once a particular task finishes execution, the worker removes it
            from the execution pool and sends a message back to the Master
            using YACS Protocol Message (***CreateMessageToMaster()***)
    """
    def __init__(self, WorkerTaskPool):  # Still need to add depending on specs
        self.tasks = dict()  # Task ID as key and duration as value
        self.taskpool = WorkerTaskPool
        self.LOCK = Lock()  # Where to use??
        self.startTime = 0
        self.endTime = 0
        self.turnoverTime = 0

    def listenForTask(self, json_protcol_message):
        """Listens for a ***createMessageToWorker()*** message and the sets
        initial variables
        """
        # Convert JSON to python dictionary
        python_protocol_message = json.loads(json_protcol_message)

        # The below 2 values are essential for the simulation or worker
        # computation
        self.task_in_message = python_protocol_message["task"][0]["task_id"]
        self.duration_in_message = (python_protocol_message["task"][0]
                                    ["duration"])

        # The below variables are essential for the CreateMessageToMaster()
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
                # Durations will be positive(non-zero) integers
                if self.tasks[task_id] != 0:
                    # Reduce the duration of the task by 1
                    self.tasks[task_id] -= 1
                else:
                    self.taskComplete(self.tasks[task_id])

            # Sleeps for 1 second until next check on the values
            time.sleep(1)
        # NOTE: Need to add the portion wherein the worker needs to listen
        # for messages if dict is empty
        # NOTE: Need to first establish communication between master and
        # worker for that for that

    def taskComplete(self, task_id): #Called by simulateWorker() when duration becomes 0 and returns JSON object of format createMessageToMaster() of YACS Protocol
        self.endTime=time.time() # End timer of the task
        self.turnoverTime=self.endTime-self.startTime #It is waiting+burst, i.e end-start in this context
        # Can also call the YACS Protocol class's createMessageToWorker() for this
        response_message_to_master={} #python dictionary for response message
        response_message_to_master["worker_id"]=self.workerID_in_message
        response_message_to_master["job_id"]=self.jobID_in_message
        response_message_to_master["task family"]=self.taskfamily_in_message
        response_message_to_master["task"]={}
        response_message_to_master["task"]["task_id"]=self.task_in_message
        response_message_to_master["task"]["start time"]=self.startTime
        response_message_to_master["task"]["end time"]=self.endTime
        response_message_to_master["task"]["task turnaround time"]=self.turnoverTime
        response_message_to_master["task"]["duration"]=self.duration_in_message
        del self.tasks[task_id] #Remove the task entry from the exec pool 
        return json.dumps(response_message_to_master) # python dict converted to JSON object
