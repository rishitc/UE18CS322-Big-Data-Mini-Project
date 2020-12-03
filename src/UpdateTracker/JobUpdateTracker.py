import time
import json
import csv
import os
from threading import Lock


class Tracker:
    """
    - This Class keeps track of the various Jobs that are created.
    - The Jobs and the Tasks associated with the jobs are tracked.
    - This Class also keeps track of the mapper reducer dependency.
    - This Class creates csv log files for future analysis.
    - The log files include:

| File Name | Contents |
|:-:|:-:|
| ```jobs.csv``` | job_id, start time, end time and duration |
| ```tasks.csv``` | job_id, task_id, start time, end time and duration |
| ```workers.csv``` | job_id, worker_id, task_id, start time and end time |
    """
    def __init__(self, algorithm):
        self.jobs = dict()
        self.jobs_time = dict()
        self.tasks_time = dict()
        self.workers_time = dict()
        self.map_tracker = dict()
        self.reduce_tracker = dict()
        self.algorithm = algorithm
        self.LOCK = Lock()

        fields_job = ['JobID', 'start_time', 'end_time', 'duration']
        fields_task = ['JobID', 'TaskID', 'start_time', 'end_time', 'duration']
        fields_worker = ['JobID', 'WorkerID', 'TaskID', 'start_time',
                         'end_time']

        # print(f"Program is at location: {os.getcwd()}")

        algorithm = os.path.join(".", "Analytics", algorithm)

        # If the folder to store the logs of the application does not exist
        if not os.path.exists(algorithm):
            print("Creating directory to store results")
            os.mkdir(algorithm)

        # Object attributes to hold the file handler, to store the logs
        self.f_jobs = open(os.path.join(algorithm, "jobs.csv"), 'w')
        self.f_tasks = open(os.path.join(algorithm, "tasks.csv"), 'w')
        self.f_workers = open(os.path.join(algorithm, "workers.csv"), 'w')

        j_writer = csv.writer(self.f_jobs, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)
        t_writer = csv.writer(self.f_tasks, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)
        w_writer = csv.writer(self.f_workers, delimiter=',', quotechar='"',
                              quoting=csv.QUOTE_MINIMAL)
        j_writer.writerow(fields_job)
        t_writer.writerow(fields_task)
        w_writer.writerow(fields_worker)
        self.job_writer = j_writer
        self.task_writer = t_writer
        self.worker_writer = w_writer
        self.flush()
        print("Job Tracker Initialized")

    def flush(self):
        self.f_jobs.flush()
        self.f_tasks.flush()
        self.f_workers.flush()

    def addJobRequest(self, parsed_json_request: dict):  # request_message):
        """
        - Gets the Request message and initialises the dictionaries
        to keep track of the jobs and associated tasks.
        - Get job_ids from request message, update jobs and tasks
        - jobs_time keeps track of time to complete a job.
        Starting time is initialized when request message is sent
        Ending time is updated when all tasks in a job are complete and a
        response message is sent tasks_time keeps track of start time and
        end time of a task.
        The start time and end time of a particular task are received in the
        response message.
        """
        # json_string = json.loads(request_message)

        # Get the job id from request string
        job_id = parsed_json_request["job_id"]

        # The jobs dictionary keeps track of jobs as well as the tasks
        # in the job
        self.jobs[job_id] = dict()

        self.map_tracker[job_id] = dict()  # Tracker for map tasks
        self.reduce_tracker[job_id] = dict()  # Tracker for reduce tasks

        # We log the start time of the job and set the end time of the job
        # as None for now
        self.jobs_time[job_id] = [time.time(), None]

        self.tasks_time[job_id] = dict()
        self.workers_time[job_id] = dict()

        # Initializing the dictionaries below
        for map_task in parsed_json_request["map_tasks"]:
            self.jobs[job_id][map_task["task_id"]] = None
            self.tasks_time[job_id][map_task["task_id"]] = None
            self.map_tracker[job_id][map_task["task_id"]] = 0

        for reduce_task in parsed_json_request["reduce_tasks"]:
            self.jobs[job_id][reduce_task["task_id"]] = None
            self.tasks_time[job_id][reduce_task["task_id"]] = None
            self.reduce_tracker[job_id][reduce_task["task_id"]] = 0

    def updateJob(self, parsed_json_request):
        """
        This method takes in the response message and performs the following
        tasks:

        - Updates task end time.
        - If all tasks composing a job are done, updates job end time.
        - Updates task stats of a worker.
        - Writes out the stats of job, task, worker to a csv file.
        - Format of task_stats is ```[start_time, end_time]```.
        """
        # json_string = json.loads(response_message)

        # Converting the Python dictionary into a JSON string
        response_message = json.dumps(parsed_json_request)
        # Get the job id from the response message
        job_id = parsed_json_request["job_id"]
        # Get the task id from the response message
        task_id = parsed_json_request["task"]["task_id"]
        # Get the worker id from the response message
        worker_id = parsed_json_request["worker_id"]
        # Get the task family from the response message
        task_fam = parsed_json_request["task family"]

        # Get task start and end time on worker
        task_stats = [parsed_json_request["task"]["start_time"],
                      parsed_json_request["task"]["end_time"]]
        self.jobs[job_id][task_id] = response_message
        # Stores start time and end time for a task
        self.tasks_time[job_id][task_id] = task_stats
        self.writeTasksCSV(job_id, task_id)

        # Store the job_id, worker_id, task_id for a particular task
        self.workers_time[job_id][worker_id] = task_stats
        self.writeWorkersCSV(job_id, worker_id, task_id)

        # If the task is a mapper task then update map_tracker else
        # update reduce tracker
        if task_fam == "map":
            self.map_tracker[job_id][task_id] = 1
        else:
            self.reduce_tracker[job_id][task_id] = 1
        '''
        Check if all tasks that compose a job are finished
        This is checked using a flag. If flag remains 1, then all tasks
        in a job are completed and the job end time is written to the
        jobs_time dictionary.
        '''
        flag = 1
        for key in self.jobs[job_id].keys():
            if self.jobs[job_id][key] is None:
                flag = 0
                break
        if flag == 1:
            self.jobs_time[job_id][1] = time.time()
            self.writeJobsCSV(job_id)

    def isMapComplete(self, jobID) -> bool:
        """
        - Performs a check whether all map tasks in a job are complete.
        - This is to maintain *map-reduce dependency*.
        """
        status = self.map_tracker[jobID].values()
        if 0 in status:
            return False
        else:
            return True

    def isReduceComplete(self, jobID) -> bool:
        """
        - Performs a check whether **all reduce tasks in a job are complete**.
        - This is to maintain *map-reduce dependency*.
        """
        status = self.reduce_tracker[jobID].values()
        if 0 in status:
            return False
        else:
            return True

    def writeJobsCSV(self, JobID):
        """
        If a job has completed, then this method is called to write
        the stats of that particular job to a log file.
        """
        row = []
        row.append(JobID)
        start = self.jobs_time[JobID][0]
        end = self.jobs_time[JobID][1]
        row.append(start)
        row.append(end)
        row.append((end-start))
        self.job_writer.writerow(row)
        self.flush()
        # Once the job has been written into the CSV file then delete
        # its entry from the dictionary
        del self.jobs_time[JobID]
        del self.jobs[JobID]
        del self.map_tracker[JobID]
        del self.reduce_tracker[JobID]
        
    def writeTasksCSV(self, JobID, TaskID):
        """
        If a task has completed, then this method is called to write the
        stats of that particular task to a log file.
        """
        row = []
        row.append(JobID)
        row.append(TaskID)
        start = self.tasks_time[JobID][TaskID][0]
        end = self.tasks_time[JobID][TaskID][1]
        row.append(start)
        row.append(end)
        row.append((end-start))
        self.task_writer.writerow(row)
        self.flush()
        # Once the task has been written into the CSV file then delete
        # its entry from the dictionary
        del self.tasks_time[JobID][TaskID]

    def writeWorkersCSV(self, JobID, WorkerID, TaskID):
        """
        Writes worker stats to a log (here CSV) file.
        """
        row = []
        row.append(JobID)
        row.append(WorkerID)
        row.append(TaskID)
        start = self.workers_time[JobID][WorkerID][0]
        end = self.workers_time[JobID][WorkerID][1]
        row.append(start)
        row.append(end)
        self.worker_writer.writerow(row)
        self.flush()
        del self.workers_time[JobID][WorkerID]

    def __del__(self):
        """
        The destructor of the class closes all the open log files.
        """
        self.flush()
        self.f_jobs.close()
        self.f_workers.close()
        self.f_tasks.close()


if __name__ == "__main__":
    # x is initially the JSON string
    x = ('{"job_id":111,"map_tasks":[{"task_id":3,"duration":5},'
         '{"task_id":77,"duration":6}],"reduce_tasks":[{"task_id":'
         '4,"duration":10},{"task_id":88,"duration":12}]}')

    # The JSON string is the parsed into a Python dictionary
    x = json.loads(x)

    JB = Tracker("Round-Robin")
    JB.addJobRequest(x)
