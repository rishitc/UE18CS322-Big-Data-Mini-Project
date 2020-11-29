import time
import os
import json # For working on JSON data
from threading import Lock


class Worker:
    """
    - This Class simulates the worker through following steps:-
    - 1) It gets YACS Protocol Message (CreateMessageToWorker()) from the Master
    - 2) It adds the particular task to its exec pool. NOTE: (Assumption? based on scheduling algorithm) Worker will not be handed any task when exec pool is full
    - 3) (Simulate) Run the tasks by decrementing the remaining_time value each second
    - 4) Once a particular task finishes exec, the Worker removes it from the exec pool and sends a message back to the Master using YACS Protocol Message 
        (CreateMessageToMaster())
    """
    def __init__(self,WorkerTaskPool): # Still need to complete
        self.tasks={} # Task ID as key and duration as value
        self.taskpool=WorkerTaskPool
        self.lock=Lock() #Where to use??
        self.startTime=0
        self.endTime=0
        self.turnoverTime=0
    
    
    def listenForTask(self,json_protcol_message):
        python_protocol_message = json.loads(json_protcol_message) #Convert JSON to python dictionary
        self.task_in_message=python_protocol_message["task"]["task_id"]
        self.duration_in_message=python_protocol_message["task"]["duration"]
        # The above 2 values are essential for the simulation/worker computation
        # The below variables are essential for the CreateMessageToMaster() YACS Protocol once the task completes exec
        self.workerID_in_message=python_protocol_message["worker_id"]
        self.jobID_in_message=python_protocol_message["job_id"]
        self.taskfamily_in_message=python_protocol_message["task family"]
        self.tasks[self.task_in_message]=self.duration_in_message #Key-Value pair (both integers) with task id as key and intial duration as value
        self.startTime=time.time()

    def simulateWorker(self):
        #while True: # Below condition seems to be better
        while (len(self.tasks)!=0):
            for i in self.tasks:
                if self.tasks[i]!=0:
                    self.tasks[i]-=1
                else:
                    taskComplete(self.tasks[i])
            time.sleep(1) # Sleeps for 1 second

    def taskComplete(self,task_id):
        self.endTime=time.time()
        self.turnoverTime=self.endTime-self.startTime
        # Can also call the YACS Protocol class's createMessageToWorker() for this
        response_message_to_master={}
        response_message_to_master["worker_id"]=self.workerID_in_message
        response_message_to_master["job_id"]=self.jobID_in_message
        response_message_to_master["task family"]=self.taskfamily_in_message
        response_message_to_master["task"]={}
        response_message_to_master["task"]["task_id"]=self.task_in_message
        response_message_to_master["task"]["start time"]=self.startTime
        response_message_to_master["task"]["end time"]=self.endTime
        response_message_to_master["task"]["task turnaround time"]=self.turnoverTime
        response_message_to_master["task"]["duration"]=self.duration_in_message
        del self.tasks[task_id]
        return json.dumps(response_message_to_master)
        