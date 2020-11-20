import os
import json
import socket
import sys
import threading
from typing import Dict

from WorkerUtils.WorkerStateTracker import StateTracker
from Scheduler.JobRequests import JobRequestHandler

BUFFER_SIZE = 4096

MASTER_SETUP_PATH = os.path.abspath(
                                     os.path.join("..",
                                                  "setup")
                                     )
print(f"{MASTER_SETUP_PATH=}")


def listenForJobRequests(requestHandler, rh_lock):
    _JOB_REQUEST_ADDR = (socket.gethostname(), 5000)

    # Setup the master socket to listen for job requests
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as jobReqSocket:
        jobReqSocket.bind(_JOB_REQUEST_ADDR)
        jobReqSocket.listen()
        clientConn, clientAddr = jobReqSocket.accept()
        while True:
            jobRequest = clientConn.recv(BUFFER_SIZE)
            _temp = json.loads(jobRequest.decode())

            # Add new job request to job request handler object
            rh_lock.acquire()
            requestHandler.addJobRequest(_temp)
            rh_lock.release()


def jobDispatcher_Random(requestHandler, rh_lock,
                         workerStateTracker, wst_lock):
    while True:
        task = None
        rh_lock.acquire()
        if not requestHandler.isEmpty():
            task = requestHandler.getWaitingTask()
        rh_lock.release()

        if task is not None:
            

        # Pick a worker at random
        . 

        # Updating the object which is tracking the worker states
        wst_lock.acquire()
        workerStateTracker.allocateSlot()
        wst_lock.release()

# def workerUpdates(workerStateTracker, wst_lock):
#     pass


if __name__ == "__main__":
    try:
        with open(os.path.join(MASTER_SETUP_PATH, "Master_Config.json"))\
                as fHandler:
            master_conf = json.load(fHandler)
    except FileNotFoundError:
        print("Unable to find the file: Master_Config.json")
        sys.exit(1)

    # Get the name of the worker config file
    workerConfFileName = master_conf["worker config file"]
    workerConfFilePath = os.path.join(MASTER_SETUP_PATH, workerConfFileName)
    try:
        with open(workerConfFilePath) as fHandler:
            # Load the data from the worker config file
            workerConf = json.load(fHandler)
    except FileNotFoundError:
        print(f"Unable to find the file: {workerConfFileName}")
        sys.exit(1)

    while input("Have the worker(s) been started, yet? [y/n]").strip().lower()\
            in ['n', 'no']:
        pass

    # Create the state tracker object
    obj_wst = StateTracker(workerConf)
    wst_lock = threading.Lock()
    rh_lock = threading.Lock()
    requestHandler = JobRequestHandler()
    obj_jrl = threading.Thread(name="Listen for Incoming Job Requests",
                               target=listenForJobRequests,
                               args=(requestHandler, rh_lock))
    obj_jd = threading.Thread(name="Job Dispatcher - Random Scheduling",
                              target=jobDispatcher_Random,
                              args=(requestHandler, rh_lock,
                                    obj_wst, wst_lock))
    # obj_wu = threading.Thread(name="Worker Updates",
    #                           target=workerUpdates,
    #                           args=(obj_wst, wst_lock))


    # Show the JSON data loaded in from the configuration file
    # print(workerConf)
    jobRequestListener = ListenForJobRequests()
    jobRequestListener.start()

    
    

