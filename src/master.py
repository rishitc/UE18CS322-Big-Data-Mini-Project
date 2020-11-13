import os
import json
import sys

from SimplifiedSocket.JobRequestSocket import JobRequestSocket
from WorkerUtils.WorkerStateTracker import StateTracker


MASTER_SETUP_PATH = os.path.abspath(
                                     os.path.join("..",
                                                  "setup")
                                     )
print(f"{MASTER_SETUP_PATH=}")

if __name__ == "__main__":
    """Setup the state tracker for the master to track the
    the worker nodes
    """
    try:
        with open(os.path.join(MASTER_SETUP_PATH, "Master_Config.json"))\
                as fHandler:
            master_conf = json.load(fHandler)
    except FileNotFoundError:
        print("Unable to find the file: Master_Config.json")
        sys.exit(1)

    # Get the name of the worker config file
    confObjFileName = master_conf["worker config file"]
    confObj = os.path.join(MASTER_SETUP_PATH, confObjFileName)
    try:
        with open(os.path.join(MASTER_SETUP_PATH, confObj)) as fHandler:
            # Load the data from the worker config file
            confObj = json.load(fHandler)
    except FileNotFoundError:
        print(f"Unable to find the file: {confObjFileName}")
        sys.exit(1)

    # print(f"{confObj=}")

    # Create the state tracker object
    obj_ct = StateTracker(confObj)
    obj_ct.showWorkerStates()

    # Setup the master socket to listen for job requests
    obj_jrs = JobRequestSocket()
    obj_jrs.socketSetup()
