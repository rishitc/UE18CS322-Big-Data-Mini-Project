# UE18CS322-Big-Data-Mini-Project
UE18CS322 Big Data Mini Project Repository

## Running Instructions
1. Make sure that you have **Python 3.8.5 or above** installed on your system
   1. In the following ```README.md```, we assume that you are using **Python 3.8.5 or above**
   2. We use the required version of **Python** in the terminal, using the command  ```python3``` 
2. Installing all the packages mentioned in ```requirements.txt```
    ```bash
    $ pip install -r requirements.txt
    ```
    - After running this command, run the below command as well. This is needed so that the analytics plots display properly:
        ```bash
        $ jupyter nbextension enable --py widgetsnbextension
        ```
3. Add the src folder to your ```PYTHONPATH``` environment variable by following steps:
   1. Open your terminal and in that, navigate into the ```src``` folder of the project
   2. Once in the ```src``` folder run the command
        ```bash
        $ pwd
        ```
        - This will give you the complete path to the ```src``` folder your are currently in.
        - Make sure to save this path returned, as it will be needed in the next steps
    1. Open your system's ```.bash_profile``` file using the command,
       ```bash
       $ nano ~/.bash_profile
       ```
       - Navigate to the bottom of the file
    2. Type in the following into the file,
        ```bash
        export PYTHONPATH="<The_path_returned_by_the_pwd_command_done_earlier>"
        ```
        - Save the file
        - Close the file
    3. Now run the below command on your terminal,
        ```bash
        $ source ~/.bash_profile
        ```
    4. Now run the below command on your terminal,
        ```bash
        $ echo $PYTHONPATH
        ```
        - You should see the path you had put as the value for the ```PYTHONPATH``` in the ```.bash_profile``` visible here
    5. **NOTE:** The same steps can also be done using the ```~/.bashrc``` file instead of the file ```~/.bash_profile```
       1. Using ```~/.bash_profile``` is recommended for systems running MacOS
       2. Any of the 2 files can used for Linux systems
4. Make sure you are in the ```src``` folder of the project. If not, then use the ```cd``` command to navigate into the ```src``` folder.
5. Run the below command in a new terminal, to start the **master**:
    ```bash
    $ python3 master.py "../setup/Copy of config.json" (RR|LL|RANDOM)
    ```
6. To start the **3 workers**, run the below commands, each in a new terminal:
    ```bash
    $ python3 worker.py 4000 1
    ```
    ```bash
    $ python3 worker.py 4001 2
    ```
    ```bash
    $ python3 worker.py 4002 3
    ```
7. Now, on the terminal in which you started the **master**, you should see the prompt:
    ```bash
    Have the 3 workers been started, yet? [y/n] 
    ```
    - Enter ```y```
    - Now wait for **~2 seconds** and you will notice that the 3 workers have connected to the master
    - Entering ```n```, will just cause the *same question/prompt* seen above to be asked again, on a new line
8. Now, start a new terminal and run the below command to start the client code:
    ```bash
    $ python3 "Copy_of_requests.py" <number_of_(job)_requests>
    ```
9.  Now, you'll notice that terminals in which the client, workers and master programs are running; there will be a **lot of debug information being output**. That's fine and it's the expected behaviour as well.
   1. If you notice **any exceptions or errors** being raised during the execution on any of the above mentioned terminals, then please do consider opening an issue on our [project repository](https://github.com/rishitc/UE18CS322-Big-Data-Mini-Project)
10. Now once you notice that there is no new output on the master and that at the end of the master program's output on the terminal, there is a message:
    ```bash
    SUCCESS: All job updates have been received!
    ```
    Then it means that the **master has completed all the jobs and corresponding tasks**, requested by the client.
11. Now that the code has completed execution, it's time to create the **logs**!... It's not as boring as you think! :smile:
    1.  Remember to **note down the number of tasks sent by the client** code. This value can be found in the last line of the output of the client code (i.e. ```Copy_of_requests.py```) as:
    ```bash
    Total number of tasks sent by client are: <TOTAL_NO_OF_TASKS_SENT_BY_CLIENT>
    ```
12. To visualize the logged data regarding tasks, jobs and workers move to the Analytics folder and run the file ```analysis.py``` as
    ```bash
    $ python3 analysis.py
    ```
    The *mean, median statistics* for jobs and tasks is displayed. **Heat Maps** and **Line Plots** are generated on separate windows to visualise workloads of the worker.
## How to store logs?
1. Create a directory under the folder ```"Logs/Without Training Wheels"``` following the naming convention:
   ```bash
   Run_<TestNumber>_<Scheduling_Algorithm_Used>
   ```
2. Create 4 files having the ```.log``` extension, namely:
   1. Master.log
   2. Worker_1.log
   3. Worker_2.log
   4. Worker_3.log
   - Remember to follow this naming convention only or else the **log analysis script** will not work!
   - All the filenames shown above are indicative of which machine's logs they will contain
3. Copy the terminal outputs and paste them into the respective files
4. Once you have populated the 4 files with their respective log outputs from the terminal output, then we move on to analysing the output

## How to check logs?
1. Go to the ```"Logs/Without Training Wheels"``` directory and execute the **log analysis script** using the command below:
    ```bash
    $ python3 "check_logs.py" <Run_TestNumber_Scheduling Algorithm>
    ```
3. Compare the task count and the individual worker counts and verify that all the counts add up
   1. Primarily make sure that **the number of tasks sent by the master**, **the number of task updates received by the master** and **the number of tasks sent by the client** are all the **same**
   2. If they are not the same then please do consider **opening an issue** on our [project repository](https://github.com/rishitc/UE18CS322-Big-Data-Mini-Project). Make sure to include all the **4 log files** and the **scheduling algorithm used** as well as other information that would be useful in *replicating the issue*

## How to generate the documentation?
1. Make sure the BASH script called ```build_docs.sh``` has **execute permission** set for the user (or user-level) you are running as, so that you can run the script successfully
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
   - In the output you may notice *PEP-224 UserWarnings*, please ignore them
   - Other than this, **no other warnings or errors** should show up. If they do then please consider **opening an issue** on our [project repository](https://github.com/rishitc/UE18CS322-Big-Data-Mini-Project)

## How do I stop the program?
1. To stop the program, simply run the script:
    ```bash
    $ ./stop-all.sh 
    ```
    - Make sure that the **execute permission** is set for the user (or user-level) you are running as, so that you can run the script successfully
    - If not then you can easily add it using the ```chmod``` command
    - Preferably the command you can run to give permissions as well as maintain system security is:
    ```bash
    $ sudo chmod 764 ./stop-all.sh
    ```
    ### or
    ```bash
    $ sudo chmod 774 ./stop-all.sh
    ```
## Contributors
* Rishit C
  * SRN: PES1201800316
* Akhil E
  * SRN: PES1201802026
* Varun T
  * SRN: PES1201802027
* T Saran Pal
  * SRN: PES1201801438

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
3. Adding encryption and key-sharing using the *SSL model* between the master and worker machines
4. All threads and related methods at the master machine
5. Threads to handle the task updates from the workers
6. Thread to store the incoming job requests from port 5000
7. Object to track the worker states
8. Thread to monitor and print out when all the tasks of all pending jobs have been dispatched to the workers and when all the updates for the same have been received at the master
9. Thread to monitor and print out when the task execution pool is empty at the worker machine
10. Create the scripts to check the logs
11. Object to track the pending job requests and return tasks as per the map-reduce
   dependency
11. Create the Communication protocol (JSON based) between master and worker nodes which will take the various parameters of the message as input
and create the json message as per the protocol format below
    - The class-methods of the class to create the message can be called as createMessageToWorker() and createMessageToMaster()
        - This method returns the required JSON string
    - Call the class as ```YACS_Protocol```

**What format does the protocol implement?**

Format for how the master sends the task (i.e. a single task) to the worker: (```createMessageToWorker()```)
```
{
    "worker_id": <worker_id>,
    "job_id": "<job_id>",
    "task_family": <("map"|"reduce")>,
    "task": {
                "task_id": "<task_id>",
                "duration": <in seconds>
             }
}
```
**Note points:**
- ```task``` can only contain one task
- ```task_family``` can only have 2 values "map" or "reduce"
- ```job_id``` has to be a string
- ```worker_id``` has to be an integer
- ```task_id``` has to be a string


Format for how the worker responds to the completion of the task (i.e. a single task): (```createMessageToMaster()```)
```
{
    "worker_id": <worker_id>,
    "job_id": "<job_id>",
    "task_family": <("map"|"reduce")>,
    "task": {
                "task_id": "<task_id>",
                "start_time": <arrival_time_of_task_at_Worker>,
                "end_time": <end_time_of_task_at_Worker>
             }
}
```
**Note points:**
- ```task``` can only contain one task
- ```job_id``` has to be a string
- ```worker_id``` has to be an integer
- ```task_id``` has to be a string
- ```task_family``` can only have 2 values "map" or "reduce"
- ```"start_time": <arrival_time_of_task_at_Worker>``` is the time as a floating point number expressed in seconds since the epoch, in UTC
- ```"end_time": <end_time_of_task_at_Worker>``` is the time as a floating point number expressed in seconds since the epoch, in UTC

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
1. [Working with Threading module in Python](https://docs.python.org/3/library/threading.html)
1. [Jupyter Widgets installation](https://ipywidgets.readthedocs.io/en/latest/user_install.html)
1. [Using queues](https://docs.python.org/3/library/queue.html#queue.Queue.join)
