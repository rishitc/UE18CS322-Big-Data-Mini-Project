import time
import json
import csv
class JobTracker:
    def __init__(self):
        self.jobs=dict()
        self.jobs_time=dict()
        self.tasks_time=dict()
        self.map_tracker=dict()
        self.reduce_tracker=dict()
    def add_jobs(self, request_message):
        #Get job_ids from request message, update jobs and tasks
        json_string=json.loads(request_message)
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
        #Initializing the dictionaries below
        for i in json_string["map_tasks"]:
            self.jobs[job_id][i["task_id"]]=None
            self.tasks_time[job_id][i["task_id"]]=None
            self.map_tracker[job_id][i["task_id"]]=0
        for i in json_string["reduce_tasks"]:
            self.jobs[job_id][i["task_id"]]=None
            self.tasks_time[job_id][i["task_id"]]=None
            self.reduce_tracker[job_id][i["task_id"]]=0
    def update_jobs(self, response_message):
        json_string=json.loads(response_message)
        #Get the job id from the response message
        job_id=json_string["job_id"]
        #get the task id from the response message
        task_id=json_string["task"][0]["task_id"]
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
    def isMapComplete(self,jobID):
        status=self.map_tracker[jobID].values()
        if 0 in status:
            return 0
        else:
            return 1
    def isReduceComplete(self,jobID):
        status=self.reduce_tracker[jobID].values()
        if 0 in status:
            return 0
        else:
            return 1
    
    def writeJobsCSV(self):
        rows=[]
        for i in self.jobs_time.keys():
            entry=[]
            entry.append(i)
            start=self.jobs_time[i][0]
            end=self.jobs_time[i][1]
            entry.append(str(start))
            entry.append(str(end))
            entry.append(str(end-start))
            rows.append(entry)
        fields=['JobID','start_time','end_time','duration']
        with open('jobs.csv','w') as f:
            write=csv.writer(f)
            write.writerow(fields)
            write.writerows(rows)
    
    def writeTasksCSV(self):
        rows=[]
        for i in self.tasks_time.keys():
            for j in self.tasks_time[i].keys:
                entry=[]
                entry.append(i)
                entry.append(j)
                start=self.tasks_time[i][j][0]
                end=self.tasks_time[i][j][1]
                entry.append(str(start))
                entry.append(str(end))
                entry.append(str(end-start))
                rows.append(entry)
        fields=['JobID','TaskID','start_time','end_time','duration']
        with open('tasks.csv','w') as f:
            write=csv.writer(f)
            write.writerow(fields)
            write.writerows(rows)
'''
x='{"job_id":111,"map_tasks":[{"task_id":3,"duration":5},{"task_id":77,"duration":6}],"reduce_tasks":[{"task_id":4,"duration":10},{"task_id":88,"duration":12}]}'
JB=JobTracker()
JB.add_jobs(x)
'''