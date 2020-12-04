import os
import sys
import json
import colored as TC


logName = sys.argv[1]

masterStats = {
               "selected tuple count": 0,
               "tasks sent to worker count": 0,
               "updates received from worker count": 0
               }
orderOfTasksSentByMaster = []
with open(os.path.join(logName, "Master.log")) as f:
    for line in f:
        if line.startswith("Selected tuple:"):
            masterStats["selected tuple count"] += 1
        if line.startswith("Sending task to worker:"):
            _temp = json.loads(line.lstrip("Sending task to worker:").strip())
            masterStats["tasks sent to worker count"] += 1
            orderOfTasksSentByMaster.append((f'{_temp["job_id"]} : '
                                             f'{_temp["task"]["task_id"]}'))
        if line.startswith("Received worker update at master:"):
            _temp = line.lstrip("Received worker update at master:").strip()
            masterStats["updates received from worker count"] += \
                len(json.loads(_temp))

print(json.dumps(masterStats, indent=4))


workerStats = [
                {"tasks received": 0, "tasks sent": 0},
                {"tasks received": 0, "tasks sent": 0},
                {"tasks received": 0, "tasks sent": 0}
               ]
workerFileList = ["Worker_1.log", "Worker_2.log", "Worker_3.log"]
for ind, workerFile in enumerate(workerFileList):
    with open(os.path.join(logName, workerFile)) as f:
        for line in f:
            if line.startswith("Task sent:"):
                workerStats[ind]["tasks sent"] += 1
            if line.startswith("Task received at worker:"):
                _temp = line.lstrip("Task received at worker:").strip()
                workerStats[ind]["tasks received"] += len(json.loads(_temp))

for ind, workerStat in enumerate(workerStats, start=1):
    print(f"Worker-{ind} Stats:", json.dumps(workerStat, indent=4), sep='\n')

print()
print('-'*80)
print()

print((f"The {TC.attr(1)}job_id : task_id{TC.attr(0)}, sent by the master to "
       "the workers are:"))
for dispatch in orderOfTasksSentByMaster:
    print(dispatch)
