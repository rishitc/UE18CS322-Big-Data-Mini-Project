import os
import sys
import json


logName = sys.argv[1]

masterStats = {
               "selected tuple count": 0,
               "tasks sent to worker count": 0,
               "updates received from worker count": 0
               }

with open(os.path.join(logName, "Master.log")) as f:
    for line in f:
        if line.startswith("Selected tuple:"):
            masterStats["selected tuple count"] += 1
        if line.startswith("Sending task to worker:"):
            masterStats["tasks sent to worker count"] += 1
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
