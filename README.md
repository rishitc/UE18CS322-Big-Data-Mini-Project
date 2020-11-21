# UE18CS322-Big-Data-Mini-Project
UE18CS322 Big Data Mini Project Repository

## Running Instructions
1. Installing all the packages mentioned in ```requirements.txt```
```bash
$ pip install -r requirements.txt
```


## Contributors
* Rishit C
* Akhil E
* Varun T
* Saran P

---

# Work Division:

### Saran:  (Plotting and Analysis of the information)
- Analyzing the results (everything in Slide 27)
- Calculates the mean and median task and job completion times for the 3 scheduling algorithms.
- Plotting the number of tasks scheduled on each machine against time, for each scheduling algorithm

- Use matplotlib or seaborn and make a line plot for each machine, with the X-Axis as time and the Y-Axis as the number of tasks scheduled 
on that machine

**Points for keep in mind:**
1. The title of the plot must show for which machine the plot has been made
1. The plots must be have the axis labelled and the marking on the axis visible
1. The size of the plot must also be big so that it looks clear
1. Finally, also make a plot with all the line plots (one for each machine) shown together so that it is possible 
to compare the performance for each machine

### Rishit: (Scheduling and Task execution request)
1. Create the 3 Scheduling algorithms to select the machine to run the tasks on
1. Sending the job to the workers using the message creation as per the YACS_Protocol class
1. Handling the SimplifiedSockets class for easy socket Communication


### Varun: (Simulation and Task completion response)
1. Simulation of workers and task execution. (Slide 13)
    - A for-loop with time.sleep() for one second will make sure the loop progresses for 1 iteration per second and every iteration decrease the remaining_duration value of each executing task in the execution pool by 1 until it reaches 0
    - This is essentially the workflow (d) in the slide 19
1. Send message using the YACS_Protocol of the details of the task completion

### Akhil: (Logging and Communication protocol)
1. Work on the job tracker for tracking job completions time stamps
1. Log the JSON information which is sent in by the workers to the master node after the task has been completed as well as log the Job completion data (this can be got from the JobTracker object)
    - More information about this can be found in the protocol format below
    - For logging use 3 separate folder (1 for each scheduling protocol)
    - In each folder keep 2 files: 1 for the Task completion time and the other for the job completion time
1. Create the Communication protocol (JSON based) between master and worker nodes which will take the various parameters of the message as input
and create the json message as per the protocol format below
    - The class-methods of the class to create the message can be called as createMessageToWorker() and createMessageToMaster()
        - This method returns the required JSON string
    - Call the class as YACS_Protocol

**What format does the protocol implement?**

Format for how the master sends the task (i.e. a single task) to the worker: (createMessageToWorker())
```
{
	"worker_id":<worker_id>,
	"job_id":<job_id>,
	"task family": <("map_tasks"|"reduce_tasks")>,
	"task":[
		{"task_id":"<task_id>","duration":<in seconds>},
	]
}
```
**Note points:**
- "task": [] can only contain one task
- task_family can only have 2 values "map_tasks" or "reduce_tasks"
- job_id has to be and integer
- Worker_id has to be and integer only
- task_id has to be a string


Format for how the worker responds to the completion of the task (i.e. a single task): (createMessageToMaster())
```
{
	"worker_id":<worker_id>,
	"job_id":<job_id>,
	"task family": <("map_tasks"|"reduce_tasks")>,
	"task":[
		{"task_id":"<task_id>",
         "start time":<arrival_time_of_task_at_Worker>,
         "end time":<end_time_of_task_in_Worker>,
		 "task completion time":<in seconds>},
	]
}
```
**Note points:**
- "task": [] can only contain one task
- job_id has to be and integer
- Worker_id has to be and integer only
- task_family can only have 2 values "map_tasks" or "reduce_tasks"
- "task completion time" has to be an float type
- "start time":<arrival_time_of_task_at_Worker> has to be a timestamp,
- "end time":<end_time_of_task_in_Worker>, has to be to be a timestamp
- "job completion time" has to a float type
-  task_id has to be a string

---

## Reference Websites
1. [JSON Library, Python Docs](https://docs.python.org/3/library/json.html)
1. [Working with JSON module in Python](https://www.w3schools.com/python/python_json.asp)
1. [Examples with explanation for using the JSON module in Python](https://realpython.com/python-json/)
1. [Socket library, Python Docs](https://docs.python.org/3/library/socket.html)
