import json
import socket
import sys
import threading
import colored as TC
import inflect

from WorkerUtils.WorkerStateTracker import StateTracker
from WorkerUtils.WorkerUpdatesTracker import UpdatesTracker

from Scheduler.JobRequests import JobRequestHandler
from Scheduler.RandomScheduling import RandomScheduler
from Scheduler.RoundRobinScheduling import RoundRobinScheduler
from Scheduler.LeastLoadedScheduling import LeastLoadedScheduler

BUFFER_SIZE = 4096
GE = inflect.engine()  # GE means Grammar Engine
PRINT_LOCK = threading.Lock()


def info_text(text):
    return f"{TC.fg(6) + TC.attr(1)}INFO:{TC.attr(0)} {text}"


def error_text(text):
    return f"{TC.fg(1) + TC.attr(1)}ERROR:{TC.attr(0)} {text}"


def listenForJobRequests(requestHandler, workerUpdatesTracker):
    _JOB_REQUEST_ADDR = (socket.gethostname(), 5000)

    # Setup the master socket to listen for job requests
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as jobReqSocket:
        jobReqSocket.bind(_JOB_REQUEST_ADDR)
        jobReqSocket.listen()
        clientConn, clientAddr = jobReqSocket.accept()

        PRINT_LOCK.acquire()
        print(info_text("Connected to client at address:"))
        print(f"IP Address: {clientAddr[0]}")
        print(f"Socket: {clientAddr[1]}")
        PRINT_LOCK.release()

        while True:
            jobRequest = clientConn.recv(BUFFER_SIZE)
            if not jobRequest:
                clientConn.close()
                break

            # Decode and parse the JSON string
            parsedJSON_Msg = json.loads(jobRequest.decode())

            # Add new job request to job request handler object
            # for task dispatch
            requestHandler.LOCK.acquire()
            requestHandler.addJobRequest(parsedJSON_Msg)
            requestHandler.LOCK.release()

            # Add new job request to job request handler object
            # for tracking dispatched tasks' completion by the
            # workers
            workerUpdatesTracker.LOCK.acquire()
            workerUpdatesTracker.addJob(parsedJSON_Msg)
            workerUpdatesTracker.LOCK.release()


def workerUpdates(workerSocket, workerStateTracker,
                  workerUpdatesTracker):
    while True:
        workerUpdate = workerSocket.recv(BUFFER_SIZE)
        if not workerUpdate:
            workerSocket.close()
            break

        parsedJSON_Msg = json.loads(workerUpdate)

        workerUpdatesTracker.LOCK.acquire()
        workerUpdatesTracker.updateJob(parsedJSON_Msg)
        workerUpdatesTracker.LOCK.release()

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
        print(error_text(f"Unable to find the file given by path:\
 {PATH_TO_CONFIG_FILE}"))
        sys.exit(1)

    WORKER_COUNT = len(workerConf['workers'])

    _ans = 'n'
    while _ans in ['n', 'no']:
        _ans = input(f"{'Have' if WORKER_COUNT > 1 else 'Has'} the\
 {WORKER_COUNT} {GE.plural_noun('worker', WORKER_COUNT)} been started,\
 yet? [y/n]").strip().lower()

    """ Creating the thread-shared objects
    """
    # Worker State Tracker Object
    obj_workerStateTracker = StateTracker(workerConf)

    # Worker updates handler object
    obj_workerUpdatesTracker = UpdatesTracker()

    # Job Request Handler Object
    obj_requestHandler = JobRequestHandler(obj_workerUpdatesTracker)

    # ---

    """ Creating the various threads needed at the master machine and
     passing in the required parameters.
     All the threads are declared as daemon threads.
     Daemon threads are those threads which are killed when the main
     program exits.
    """
    jobRequestThread = threading.Thread(name=("Listen for Incoming Job"
                                              "Requests"),
                                        target=listenForJobRequests,
                                        args=(obj_requestHandler))
    jobRequestThread.daemon = True

    taskDispatchThread = None
    if TYPE_OF_SCHEDULING == "RANDOM":
        taskDispatchThread = threading.Thread(name=("Job Dispatcher -"
                                                    "Random Scheduling"),
                                              target=RandomScheduler.
                                              jobDispatcher,
                                              args=(obj_requestHandler,
                                                    obj_workerStateTracker))
    elif TYPE_OF_SCHEDULING == "RR":
        taskDispatchThread = threading.Thread(name=("Job Dispatcher -"
                                                    "Round-Robin Scheduling"),
                                              target=RoundRobinScheduler.
                                              jobDispatcher,
                                              args=(obj_requestHandler,
                                                    obj_workerStateTracker,
                                                    WORKER_COUNT))
    elif TYPE_OF_SCHEDULING == "LL":
        taskDispatchThread = threading.Thread(name=("Job Dispatcher -"
                                                    "Least-Loaded Scheduling"),
                                              target=LeastLoadedScheduler.
                                              jobDispatcher,
                                              args=(obj_requestHandler,
                                                    obj_workerStateTracker,
                                                    WORKER_COUNT))
    else:
        print(error_text("Invalid value entered for type of scheduling!"))
        sys.exit(1)

    taskDispatchThread.daemon = True

    WORKER_UPDATES_PORT = 5001
    WORKER_UPDATES_ADDR = (socket.gethostname(), WORKER_UPDATES_PORT)
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as \
         worker_updates_socket:
        worker_updates_socket.bind(WORKER_UPDATES_ADDR)

        # Put the socket into listening mode
        worker_updates_socket.listen(WORKER_COUNT)
        PRINT_LOCK.acquire()
        print(info_text(("Listening to updates from the workers on port: "
                         f"{WORKER_UPDATES_PORT}")))
        PRINT_LOCK.release()

        # List to hold the threads listening to updates from the workers
        workerUpdateThreads = []

        # A forever loop until client wants to exit
        for _ in range(WORKER_COUNT):
            # Establish connection with client
            workerSocket, workerAddress = worker_updates_socket.accept()

            # Get the worker number from the newly connected worker
            WORKER_NUMBER = workerSocket.recv(BUFFER_SIZE).decode()
            # Printing connection updates
            PRINT_LOCK.acquire()
            print(info_text("Connected to worker at address:"))
            print(f"IP Address: {workerAddress[0]}")
            print(f"Socket: {workerAddress[1]}")
            PRINT_LOCK.release()

            # Start a new thread and return its thread object
            _temp = threading.Thread(target=workerUpdates,
                                     name=(f"Worker-{WORKER_NUMBER} Update "
                                           "Listener"),
                                     args=(workerSocket,
                                           obj_workerStateTracker,
                                           obj_workerUpdatesTracker))
            _temp.daemon = True

            # Store the thread object in a list
            workerUpdateThreads.append(_temp)

        print(f"{workerUpdateThreads=}")

    """ Wait for all the threads to finish
    """
    # Wait for the thread listening for incoming job requests to finish
    jobRequestThread.join()

    # Wait for the thread dispatching tasks to the worker to finish
    taskDispatchThread.join()

    # Wait for the threads listening for worker updates to finish
    for updateThread in workerUpdateThreads:
        updateThread.join()

    # Closing all task dispatch sockets to the workers
    obj_workerStateTracker.closeDispatchTaskSockets()
