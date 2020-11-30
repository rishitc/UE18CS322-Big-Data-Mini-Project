# UE18CS322-Big-Data-Mini-Project
UE18CS322 Big Data Mini Project Repository

## Running Instructions
1. Installing all the packages mentioned in ```requirements.txt```
    ```bash
    $ pip install -r requirements.txt
    ```
1. Add the src folder to your ```PYTHONPATH``` environment variable by following steps:
   1. Open your terminal and in that, navigate into the ```src``` folder of the project
   2. Once in the ```src``` folder run the command
        ```bash
        $ pwd
        ```
        - This will give you the complete path to the ```src``` folder your are currently in.
        - Make sure to save this path returned, as it will be needed in the next steps
    3. Open your system's ```.bash_profile``` file using the command,
       ```bash
       $ nano ~/.bash_profile
       ```
       - Navigate to the bottom of the file
    4. Type in the following into the file,
        ```bash
        export PYTHONPATH="<The_path_returned_by_the_pwd_command_done_earlier>"
        ```
        - Save the file
        - Close the file
    5. Now run the below command on your terminal,
        ```bash
        $ source ~/.bash_profile
        ```
    6. Now run the below command on your terminal,
        ```bash
        $ echo $PYTHONPATH
        ```
        - You should see the path you had put as the value for the ```PYTHONPATH``` in the ```.bash_profile``` visible here
    7. **NOTE:** The same steps can also be done using the ```~/.bashrc``` file instead of the file ```~/.bash_profile```
       1. Using ```~/.bash_profile``` is recommended for systems running MacOS
       2. Any of the 2 files can used for Linux systems

## How to generate the documentation?
1. Make sure the BASH script called ```build_docs.sh``` has **execute permission** set for the user you
   are running as.
    - If not then you can easily add it using the ```chmod``` command
    - Preferably the command you can run to give permissions as well as maintain system security is:
    ```bash
    $ sudo chmod 764 ./build_docs.sh
    ```
    ### or
    ```bash
    $ sudo chmod 774 ./build_docs.sh
    ```
2. The run the command:
   ```bash
   $ ./build_docs.sh
   ```
   - In the output you may notice *PEP-224 UserWarnings*, please ignore them.
   - Other than this, **no other warnings or errors** should show up. If they do then please consider **opening an issue** on our [project repository](https://github.com/rishitc/UE18CS322-Big-Data-Mini-Project)

## Contributors
* Rishit C
* Akhil E
* Varun T
* Saran P

---

# Note Points
1. The starting time of the job is the time at which the worker received the first **map task** of the job.
   1. This value will be equal to the smallest value for the ```start time``` field among all the acknowledgement messages sent by the workers to the master for a particular job
2. The ending time of the job is the time at which the worker finishes the last **reduce task** of the job.
   1. This value will be equal to the largest value for the ```end time``` field among all the acknowledgement messages sent by the workers to the master for a particular job

---

# Work Division:

### Saran:  (Plotting and Analysis of the information)
- Analyzing the results (everything in Slide 27)
- Calculates the mean and median task and job completion times for the 3 scheduling algorithms.
- Plotting the number of tasks scheduled on each machine against time, for each scheduling algorithm

- Use [```pandas```](https://pandas.pydata.org/) and/or [```matplotlib```](https://matplotlib.org/) and/or [```seaborn```](https://seaborn.pydata.org/) and make a line plot for each machine, with the X-Axis as time and the Y-Axis as the number of tasks scheduled 
on that machine

**Points for keep in mind:**
1. The title of the plot must show for which machine the plot has been made
1. The plots must be have the axis labelled and the marking on the axis visible
1. The size of the plot must also be big so that it looks clear
1. Finally, also make a plot with all the line plots (one for each machine) shown together so that it is possible to compare the performance for each machine

---

### Rishit: (Scheduling and Task execution request)
1. Finish the 3 Scheduling algorithms to select the worker machine to run the task on
2. Sending the job to the workers using the message creation as per the ```YACS_Protocol``` class
3. Thread to store the incoming job requests from port 5000
4. Object to track the worker states
5. Object to track the pending job requests and return tasks as per the map-reduce
   dependency
6. Create the Communication protocol (JSON based) between master and worker nodes which will take the various parameters of the message as input
and create the json message as per the protocol format below
    - The class-methods of the class to create the message can be called as createMessageToWorker() and createMessageToMaster()
        - This method returns the required JSON string
    - Call the class as ```YACS_Protocol```

**What format does the protocol implement?**

Format for how the master sends the task (i.e. a single task) to the worker: (```createMessageToWorker()```)
```
{
    "worker_id": <worker_id>,
    "job_id": <job_id>,
    "task family": <("map_tasks"|"reduce_tasks")>,
    "task": {
                "task_id": "<task_id>",
                "duration": <in seconds>
             }
}
```
**Note points:**
- "task": [] can only contain one task
- task_family can only have 2 values "map_tasks" or "reduce_tasks"
- job_id has to be an integer
- worker_id has to be an integer only
- task_id has to be a string


Format for how the worker responds to the completion of the task (i.e. a single task): (```createMessageToMaster()```)
```
{
    "worker_id":<worker_id>,
    "job_id":<job_id>,
    "task family": <("map_tasks"|"reduce_tasks")>,
    "task": {
                "task_id": "<task_id>",
                "start time": <arrival_time_of_task_at_Worker>,
                "end time": <end_time_of_task_in_Worker>
             }
}
```
**Note points:**
- "task": [] can only contain one task
- job_id has to be an integer
- Worker_id has to be an integer only
- task_family can only have 2 values "map_tasks" or "reduce_tasks"
- "task completion time" has to be an float type
- "start time":<arrival_time_of_task_at_Worker> has to be a timestamp,
- "end time":<end_time_of_task_in_Worker>, has to be to be a timestamp
- "job completion time" has to be a float type
-  task_id has to be a string

---

### Varun: (Simulation and Task completion response)
1. Simulation of workers and task execution. (ref. Slide 13)
    - A for-loop with ```time.sleep()``` for one second will make sure the loop progresses for 1 iteration per second and every iteration decrease the remaining_duration value of each executing task in the execution pool by 1 until it reaches 0
    - This is essentially the workflow (d) in the slide 19
1. Send message using the ```YACS_Protocol``` of the details of the task completion
1. Other useful slides while creating the worker code: 8, 9, 18, 21, 24, 25'
1. Connect to the master to share updates of on going tasks
1. Wait for the master to connect to worker, so that the master can start sending tasks to it

---

### Akhil: (Logging and Communication protocol)
1. Work on the job tracker (i.e. ```JobTracker``` object) for tracking job completions time stamps
   1. ```isMapComplete(jobID)``` to check if all the map tasks of a job have been completed
   2. ```isReduceComplete(jobID)``` to check if all the reduce tasks of a job have been completed
   3. ```addJob(job_request)``` to add the setup the tracking for the tasks of the job
      1. ```job_request``` is essentially the input JSON string from the client after using json.loads() on it
   4. ```updateJob(task_completion_response_from_worker)``` to update the state of the job completion, as per message from the worker sent as parameter: ```task_completion_response_from_worker```
      1. ```task_completion_response_from_worker``` is essentially the input JSON string from the client after using json.loads() on it
2. Log the JSON information which is sent in by the workers to the master node after the task has been completed as well as log the Job completion data (this can be got from the ```JobTracker``` object)
    - More information about this can be found in the protocol format above
    - For logging use 3 separate folder (1 for each scheduling protocol)
    - In each folder keep 2 files: 1 for the Task completion time and the other for the job completion time
    - Make sure to record the timestamps of the events accurately and are able to perform the required analysis.

---

## Reference Websites
1. [JSON Library, Python Docs](https://docs.python.org/3/library/json.html)
1. [Working with JSON module in Python](https://www.w3schools.com/python/python_json.asp)
1. [Examples with explanation for using the JSON module in Python](https://realpython.com/python-json/)
1. [Socket library, Python Docs](https://docs.python.org/3/library/socket.html)
1. [Setting up your PYTHONPATH](https://bic-berkeley.github.io/psych-214-fall-2016/using_pythonpath.html)
