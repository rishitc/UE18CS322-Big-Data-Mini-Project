import time
import json
import csv
import os
from threading import Lock


class Tracker:
    """
    This Class keeps track of the various Jobs that are created.
    The Jobs and the Tasks associated with the jobs are tracked.
    This Class also keeps track of the mapper reducer dependency.
    This Class creates csv log files for future analysis.
    The log files include:
        *  jobs.csv    -> includes job_id, start time, end time and duration
        *  tasks.csv   -> includes job_id, task_id, start time, end time and
                          duration
        *  workers.csv -> includes job_id, worker_id, task_id, start time and
                          end time
    """
    def __init__(self, algorithm):
        self.jobs = dict()
        self.jobs_time = dict()
        self.tasks_time = dict()
        self.workers_time = dict()
        self.map_tracker = dict()
        self.reduce_tracker = dict()
        self.algo = algorithm
        self.LOCK = Lock()

        fields_job = ['JobID', 'start_time', 'end_time', 'duration']
        fields_task = ['JobID', 'TaskID', 'start_time', 'end_time', 'duration']
        fields_worker = ['JobID', 'WorkerID', 'TaskID', 'start_time',
                         'end_time']

        # If the folder to store the logs of the application does not exist
        if not os.path.exists(algorithm):
            os.mkdir(algorithm)

        # Object attributes to hold the file handler, to store the logs
        self.f_jobs = open(os.path.join(algorithm, "jobs.csv"), 'w')
        self.f_tasks = open(os.path.join(algorithm, "tasks.csv"), 'w')
        self.f_workers = open(os.path.join(algorithm, "workers.csv"), 'w')

        j_writer = csv.writer(self.f_jobs)
        t_writer = csv.writer(self.f_tasks)
        w_writer = csv.writer(self.f_workers)
        j_writer.writerow(fields_job)
        t_writer.writerow(fields_task)
        w_writer.writerow(fields_worker)
        self.job_writer = j_writer
        self.task_writer = t_writer
        self.worker_writer = w_writer

    def addJob(self, request_message):
        """
        Gets the Request message and initialises the dictionaries
        to keep track of the jobs and associated tasks
        """
        #Get job_ids from request message, update jobs and tasks
        json_string=json.loads(request_message)
        #json_string=request_message
        #Get the job id from request string
        job_id=json_string["job_id"]
        #jobs dictionary keeps track of jobs and tasks in the job
        self.jobs[job_id]=dict()
        #Map tracker
        self.map_tracker[job_id]=dict()
        #Reduce tracker
        self.reduce_tracker[job_id]=dict()
        '''
        jobs_time keeps track of time to complete a job.
        Starting time is initialized when request message is sent
        Ending time is updated when all tasks in a job are complete and a response message is sent
        '''
        self.jobs_time[job_id]=[time.time(),None]
        '''
        tasks_time keeps track of start time and end time of a task
        The start time and end time of a particular task are received in the response message
        '''
        self.tasks_time[job_id]=dict()
        self.workers_time[job_id]=dict()
        #Initializing the dictionaries below
        for i in json_string["map_tasks"]:
            self.jobs[job_id][i["task_id"]]=None
            self.tasks_time[job_id][i["task_id"]]=None
            self.map_tracker[job_id][i["task_id"]]=0
        for i in json_string["reduce_tasks"]:
            self.jobs[job_id][i["task_id"]]=None
            self.tasks_time[job_id][i["task_id"]]=None
            self.reduce_tracker[job_id][i["task_id"]]=0
            
    def updateJob(self, response_message):
        """
        Takes in the response message and 
        *  Updates task end time
        *  If all tasks composing a job are done, updates job end time
        *  Updates task stats of a worker
        *  Writes out the stats of job, task, worker to a csv file
        """
        json_string=json.loads(response_message)
        #json_string=response_message
        #Get the job id from the response message
        job_id=json_string["job_id"]
        #get the task id from the response message
        task_id=json_string["task"][0]["task_id"]
        #Get the worker id
        worker_id=json_string["worker_id"]
        #Get the task family
        task_fam=json_string["task family"]
        #Get task start and end time on worker
        '''
        Format of task_stats is [start_time,end_time]
        '''
        task_stats=[json_string["task"][0]["start time"],json_string["task"][0]["end time"]]
        self.jobs[job_id][task_id]=response_message
        #Stores start time and end time for a task
        self.tasks_time[job_id][task_id]=task_stats
        self.writeTasksCSV(job_id,task_id)
        #Store the job_id, worker_id, task_id for a particular task
        self.workers_time[job_id][worker_id]=task_stats
        self.writeWorkersCSV(job_id, worker_id, task_id)
        #If the task is a mapper task update map_tracker else update reduce tracker
        if task_fam=="map tasks":
            self.map_tracker[job_id][task_id]=1
        else:
            self.reduce_tracker[job_id][task_id]=1
        '''
        Check if all tasks that compose a job are finished
        This is checked using a flag. If flag remains 1, then all tasks
        in a job are completed and the job end time is written to the jobs_time dictionary
        '''
        flag=1
        for key in self.jobs[job_id].keys:
            if self.jobs[job_id][key]==None:
                flag=0
                break
        if flag==1:
            self.jobs_time[job_id][1]=time.time()
            self.writeJobsCSV(job_id)
            
    def isMapComplete(self,jobID):
        """
        performs a check whether all map tasks in a job are complete
        This is to maintain map-reduce dependency
        """
        status=self.map_tracker[jobID].values()
        if 0 in status:
            return 0
        else:
            return 1
        
    def isReduceComplete(self,jobID):
        """
        performs a check whether all reduce tasks in a job are complete
        This is to maintain map-reduce dependency
        """
        status=self.reduce_tracker[jobID].values()
        if 0 in status:
            return 0
        else:
            return 1
    
    def writeJobsCSV(self,JobID):
        """
        If a job is completed, writes the stats of that particular
        job to a log file.
        """
        row=[]
        row.append(JobID)
        start=self.jobs_time[JobID][0]
        end=self.jobs_time[JobID][1]
        row.append(start)
        row.append(end)
        row.append((end-start))
        self.job_writer.writerow(row)
        del self.jobs_time[JobID]

    def writeTasksCSV(self,JobID,TaskID):
        """
        If a task is completed, writes the stats of that particular
        task to a log file.
        """
        row=[]
        row.append(JobID)
        row.append(TaskID)
        start=self.tasks_time[JobID][TaskID][0]
        end=self.tasks_time[JobID][TaskID][1]
        row.append(start)
        row.append(end)
        row.append((end-start))
        self.task_writer.writerow(row)
        del self.tasks_time[JobID][TaskID]
    
    def writeWorkersCSV(self,JobID,WorkerID,TaskID):
        """
        Writes worker stats to a log file
        """
        row=[]
        row.append(JobID)
        row.append(WorkerID)
        row.append(TaskID)
        start=self.workers_time[JobID][WorkerID][0]
        end=self.workers_time[JobID][WorkerID][1]
        row.append(start)
        row.append(end)
        self.worker_writer.writerow(row)
        del self.workers_time[JobID][WorkerID]
        
    def closeFiles(self):
        """
        This closes all the open log files
        """
        self.f_jobs.close()
        self.f_workers.close()
        self.f_tasks.close()

x='{"job_id":111,"map_tasks":[{"task_id":3,"duration":5},{"task_id":77,"duration":6}],"reduce_tasks":[{"task_id":4,"duration":10},{"task_id":88,"duration":12}]}'
JB=JobTracker("rr")
JB.addJob(x)
