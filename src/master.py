import json
import socket
import sys
import threading
import random
import time
import colored as TC
import inflect

from WorkerUtils.WorkerStateTracker import StateTracker
from Scheduler.JobRequests import JobRequestHandler

BUFFER_SIZE = 4096
GRAMMAR_ENGINE = inflect.engine()


def info_text(text):
    return f"{TC.fg(6)}{TC.attr(1)}INFO:{TC.attr(0)} {text}"


def error_text(text):
    return f"{TC.fg(1)}{TC.attr(1)}ERROR:{TC.attr(0)} {text}"


def listenForJobRequests(requestHandler):
    _JOB_REQUEST_ADDR = (socket.gethostname(), 5000)

    # Setup the master socket to listen for job requests
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as jobReqSocket:
        jobReqSocket.bind(_JOB_REQUEST_ADDR)
        jobReqSocket.listen()
        clientConn, clientAddr = jobReqSocket.accept()
        print(info_text("Connected to client at address:"))
        print(f"IP Address: {clientAddr[0]}")
        print(f"Socket: {clientAddr[1]}")
        while True:
            jobRequest = clientConn.recv(BUFFER_SIZE)
            if not jobRequest:
                clientConn.close()
                break

            # Decode and parse the JSON string
            _temp = json.loads(jobRequest.decode())

            # Add new job request to job request handler object
            requestHandler.LOCK.acquire()
            requestHandler.addJobRequest(_temp)
            requestHandler.LOCK.release()


def jobDispatcher_Random(requestHandler, workerStateTracker):
    while True:
        jobID_family_task = None
        requestHandler.LOCK.acquire()
        if not requestHandler.isEmpty():
            jobID_family_task = requestHandler.getWaitingTask()
        requestHandler.LOCK.release()

        # If there is a Task that needs to be executed
        if jobID_family_task is not None:
            # Initially we have not found a worker with a free slot
            workerFound = False

            while workerFound is False:  # Until a free worker is not found
                workerStateTracker.LOCK.acquire()
                # Pick a worker at random
                _temp = random.choice(workerStateTracker.workerIDs)

                # If the worker has a free slot
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
                    # 1. We dispatch the job to the worker
                    # 2. Update its state
                    workerStateTracker.getWorkerSocket(_temp)\
                        .sendall(protocolMsg)
                    workerStateTracker.allocateSlot(_temp)
                workerStateTracker.LOCK.release()

                # Sleep for a second to allow for the workerStateTracker
                # to be updated by the thread: workerUpdates
                time.sleep(1)

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
        print(error_text(f"Unable to find the file given by path: \
{PATH_TO_CONFIG_FILE}"))
        sys.exit(1)

    WORKER_COUNT = len(workerConf['workers'])
    while input(f"{'Have' if  WORKER_COUNT > 1 else 'Has'} the {} worker{'s' if } been started, yet? [y/n]").strip().lower()\
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
        print(error_text("Invalid value entered for type of scheduling!"))
        sys.exit(1)

    """ Create the required threads on the master machine, passing in the
    required parameters. Eventhough the variables created here are global
    it is better for the sake of clarity to pass in the variables
    which you want the function to work with as arguments to it
    """
    obj_jd = threading.Thread(name="Job Dispatcher - Random Scheduling",
                              target=jobDispatcher_Random,
                              args=(requestHandler, obj_wst))

    WORKER_UPDATES_PORT = 5000
    worker_updates_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    worker_updates_socket.bind((socket.gethostname(), WORKER_UPDATES_PORT))
    print(info_text(f"Listening to updates from the workers on port: \
{WORKER_UPDATES_PORT}")

    worker_updates_socket.listen()

    obj_wu = threading.Thread(name="Worker Updates",
                              target=workerUpdates,
                              args=(workerSocket, workerStateTracker,
                                    wst_lock, jobTracker, jt_lock))


    # Show the JSON data loaded in from the configuration file
    # print(workerConf)
    jobRequestListener = ListenForJobRequests()
    jobRequestListener.start()

    
    

