import os
import json
import socket
import sys
import threading
import random
import time
import colored as TC


from WorkerUtils.WorkerStateTracker import StateTracker
from Scheduler.JobRequests import JobRequestHandler

BUFFER_SIZE = 4096

MASTER_SETUP_PATH = os.path.abspath(
                                     os.path.join("..",
                                                  "setup")
                                     )
print(f"{MASTER_SETUP_PATH=}")


def listenForJobRequests(requestHandler):
    _JOB_REQUEST_ADDR = (socket.gethostname(), 5000)

    # Setup the master socket to listen for job requests
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as jobReqSocket:
        jobReqSocket.bind(_JOB_REQUEST_ADDR)
        jobReqSocket.listen()
        clientConn, clientAddr = jobReqSocket.accept()
        while True:
            jobRequest = clientConn.recv(BUFFER_SIZE)
            if not jobRequest:
                clientConn.close()
                break

            _temp = json.loads(jobRequest.decode())

            # Add new job request to job request handler object
            requestHandler.LOCK.acquire()
            requestHandler.addJobRequest(_temp)
            requestHandler.LOCK.release()


def jobDispatcher_Random(requestHandler, rh_lock,
                         workerStateTracker):
    while True:
        jobID_family_task = None
        rh_lock.acquire()
        if not requestHandler.isEmpty():
            jobID_family_task = requestHandler.getWaitingTask()
        rh_lock.release()

        # If there is a Task that needs to be executed
        if jobID_family_task is not None:
            # Initially we have not found a worker with a free slot
            workerFound = False

            while workerFound is False:  # Until a free worker is not found
                workerStateTracker.LOCK.acquire()
                # Pick a worker at random
                _temp = random.choice(workerStateTracker.workerIDs)
                if workerStateTracker.isWorkerFree(_temp):
                    # Create the JSON protocol message
                    protocolMsg = (YACS_Protocol
                                   .createMessageToWorker
                                   (
                                       job_ID=jobID_family_task[0],
                                       task_family=jobID_family_task[1],
                                       task_ID=jobID_family_task[2]["task_id"],
                                       duration=(jobID_family_task[2]
                                                 ["duration"]),
                                       worker_ID=_temp
                                   ))
                    # Once a worker with a free slot is found then
                    # we dispatch the job to the worker and update its
                    # state
                    workerStateTracker.getWorkerSocket(_temp)\
                        .sendall(protocolMsg)
                    workerStateTracker.allocateSlot(_temp)
                workerStateTracker.LOCK.release()
                # Sleep for half a second to allow for the workerStateTracker
                # to be updated by the thread: workerUpdates
                time.sleep(0.5)

        # Updating the object which is tracking the worker states
        workerStateTracker.LOCK.acquire()
        workerStateTracker.allocateSlot()
        workerStateTracker.LOCK.release()


def workerUpdates(workerSocket, workerStateTracker,
                  jobTracker):
    while True:
        workerUpdate = workerSocket.recv(BUFFER_SIZE)
        if not workerUpdate:
            workerSocket.close()
            break

        parsedJSON_Msg = json.loads(workerUpdate)

        jobTracker.LOCK.acquire()
        jobTracker.updateJob(parsedJSON_Msg)
        jobTracker.LOCK.release()

        workerStateTracker.LOCK.acquire()
        workerStateTracker.freeSlot(parsedJSON_Msg["worker_id"])
        workerStateTracker.LOCK.release()


if __name__ == "__main__":
    PATH_TO_CONFIG_FILE = sys.argv[1]
    TYPE_OF_SCHEDULING = sys.argv[2]

    try:
        with open(PATH_TO_CONFIG_FILE) as fHandler:
            # Load the data from the worker config file
            workerConf = json.load(fHandler)
    except FileNotFoundError:
        print(f"{TC.fg(1)}{TC.attr(1)}ERROR:{TC.attr(0)} \
Unable to find the file given by path: {PATH_TO_CONFIG_FILE}")
        sys.exit(1)

    while input("Have the worker(s) been started, yet? [y/n]").strip().lower()\
            in ['n', 'no']:
        pass

    #  Initialize the random number generator.
    random.seed()

    obj_wst = StateTracker(workerConf)  # Worker State Tracker Object
    requestHandler = JobRequestHandler()  # Job Request Handler Object

    obj_jrl = threading.Thread(name="Listen for Incoming Job Requests",
                               target=listenForJobRequests,
                               args=(requestHandler))

    if TYPE_OF_SCHEDULING == "RANDOM":
        pass
    elif TYPE_OF_SCHEDULING == "RR":
        pass
    elif TYPE_OF_SCHEDULING == "LL":
        pass
    else:
        print(f"{TC.fg(1)}{TC.attr(1)}ERROR:{TC.attr(0)} Invalid value \
entered for type of scheduling!")
        sys.exit(1)

    """ Create the required threads on the master machine, passing in the
    required parameters. Eventhough the variables created here are global
    it is better for the sake of clarity to pass in the variables
    which you want the function to work with as arguments to it
    """
    obj_jd = threading.Thread(name="Job Dispatcher - Random Scheduling",
                              target=jobDispatcher_Random,
                              args=(requestHandler, obj_wst))
    
    obj_wu = threading.Thread(name="Worker Updates",
                              target=workerUpdates,
                              args=(workerSocket, workerStateTracker,
                                    wst_lock, jobTracker, jt_lock))


    # Show the JSON data loaded in from the configuration file
    # print(workerConf)
    jobRequestListener = ListenForJobRequests()
    jobRequestListener.start()

    
    

