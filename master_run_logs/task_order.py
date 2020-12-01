import sys
import json

TOTAL_TASK_COUNT = 0

with open(sys.argv[1]) as fhandler:
    for line in fhandler:
        if line.startswith("Sending task to worker:"):
            _temp: str = line.lstrip("Sending task to worker: ").strip()
            _temp = json.loads(_temp)
            print(f"{_temp['task family']} : {_temp['task']['task_id']}")
            TOTAL_TASK_COUNT += 1

print("-"*80)
print(f"{TOTAL_TASK_COUNT=}")
