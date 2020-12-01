import json
import socket
import sys
import threading
from typing import List, Optional, Tuple
import colored as TC
from colored.colored import attr
import inflect

from WorkerUtils.WorkerStateTracker import StateTracker
from UpdateTracker.JobUpdateTracker import Tracker as JobUpdateTracker

from Scheduler.JobRequests import JobRequestHandler
from Scheduler.RandomScheduling import RandomScheduler
from Scheduler.RoundRobinScheduling import RoundRobinScheduler
from Scheduler.LeastLoadedScheduling import LeastLoadedScheduler

BUFFER_SIZE: int = 4096

# Error codes to return to the shell
# The Unix programs' style for error codes has
# been used here
MISSING_CMD_LINE_ARGS: int = 2
BROKEN_CONFIG_FILE_PATH: int = 1

GE = inflect.engine()  # GE means Grammar Engine

# This lock is used to get access to print onto the standard output
PRINT_LOCK = threading.Lock()


def info_text(text):
    return f"{TC.fg(6) + TC.attr(1)}INFO:{TC.attr(0)} {text}"


def error_text(text):
    return f"{TC.fg(1) + TC.attr(1)}ERROR:{TC.attr(0)} {text}"


def listenForJobRequests(jobRequestHandler: JobRequestHandler,
                         jobUpdateTracker: JobUpdateTracker):
    """```listenForJobRequests``` listens for new job requests from the client
    code

    **param** ```jobRequestHandler```: Used to track the task dispath status of
    the job

    **type** ```jobRequestHandler```: JobRequestHandler

    **param** ```jobUpdateTracker```: Used to track the updates from the
    workers about the tasks assigned belonging to the different jobs

    **type** ```jobUpdateTracker```: JobUpdateTracker
    """
    _JOB_REQUEST_ADDR: Tuple[str, int] = (socket.gethostname(), 5000)

    PRINT_LOCK.acquire()
    print("Inside listenForJobRequests")
    PRINT_LOCK.release()

    # Setup the master socket to listen for job requests
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as jobReqSocket:
        jobReqSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        jobReqSocket.bind(_JOB_REQUEST_ADDR)
        while True:
            jobReqSocket.listen()
            clientConn, clientAddr = jobReqSocket.accept()

            PRINT_LOCK.acquire()
            print(f"Something connected to me!! {clientAddr}")
            PRINT_LOCK.release()

            PRINT_LOCK.acquire()
            print(info_text("Connected to client at address:"))
            print(f"IP Address: {clientAddr[0]}")
            print(f"Socket: {clientAddr[1]}")
            PRINT_LOCK.release()

            # while True:
            jobRequest = clientConn.recv(BUFFER_SIZE)
            if not jobRequest:
                clientConn.close()
                break

            # Decode and parse the JSON string
            parsedJSON_Msg = json.loads(jobRequest.decode())

            # Add new job request to job request handler object
            # for task dispatch
            jobRequestHandler.LOCK.acquire()
            jobRequestHandler.addJobRequest(parsedJSON_Msg)
            jobRequestHandler.LOCK.release()

            # Add new job request to job request handler object
            # for tracking dispatched tasks' completion by the
            # workers
            jobUpdateTracker.LOCK.acquire()
            jobUpdateTracker.addJobRequest(parsedJSON_Msg)
            jobUpdateTracker.LOCK.release()

            clientConn.close()


def workerUpdates(workerSocket: socket.socket,
                  workerStateTracker: StateTracker,
                  jobUpdateTracker: JobUpdateTracker):
    """```workerUpdates``` captures the updates from the worker as and when
    they complete the tasks assigned to them, and respond back

    **param** ```workerSocket```: The socket object for listening to the
    specific worker's updates

    **type** ```workerSocket```: socket

    **param** ```workerStateTracker```: Tracks the states of the worker nodes
    as to how many free slots do they have

    **type** ```workerStateTracker```: StateTracker

    **param** ```jobUpdateTracker```: Tracks the jobs assigned to the workers,
    and their corresponding updates

    **type** ```jobUpdateTracker```: JobUpdateTracker
    """
    while True:
        workerUpdate = workerSocket.recv(BUFFER_SIZE)
        if not workerUpdate:
            workerSocket.close()
            break

        parsedJSON_Msg = json.loads(workerUpdate)

        jobUpdateTracker.LOCK.acquire()
        jobUpdateTracker.updateJob(parsedJSON_Msg)
        jobUpdateTracker.LOCK.release()

        workerStateTracker.LOCK.acquire()
        workerStateTracker.freeSlot(parsedJSON_Msg["worker_id"])
        workerStateTracker.LOCK.release()


if __name__ == "__main__":
    # Make sure the required command line arguments are passed in
    PATH_TO_CONFIG_FILE: Optional[str] = None
    TYPE_OF_SCHEDULING: Optional[str] = None

    try:
        PATH_TO_CONFIG_FILE = sys.argv[1]
        TYPE_OF_SCHEDULING = sys.argv[2]
    except IndexError as e:
        print(f"{TC.attr(1)+TC.attr(5)+TC.fg('red')}ERROR:{attr(0)} "
              "Missing command line arguments: "
              f"{TC.attr(1)+TC.attr(4)}PATH_TO_CONFIG_FILE{TC.attr(0)}"
              f" or {TC.attr(1)+TC.attr(4)}TYPE_OF_SCHEDULING{TC.attr(0)}"
              f" or {TC.attr(1)}both!{TC.attr(0)}")
        print(e)
        sys.exit(MISSING_CMD_LINE_ARGS)

    if TYPE_OF_SCHEDULING not in ["LL", "RR", "RANDOM"]:
        raise ValueError((f"{TC.attr(1)}TYPE_OF_SCHEDULING{TC.attr(0)} is not "
                          f"of type: {TC.attr(1)}\"RANDOM\"{TC.attr(0)} or "
                          f"{TC.attr(1)}\"RR\"{TC.attr(0)} "
                          f"or {TC.attr(1)}\"LL\"{TC.attr(0)}!")
                         )

    # Making sure that the configuration file can be opened
    try:
        with open(PATH_TO_CONFIG_FILE) as fHandler:
            # Load the data from the worker config file
            workerConf: dict = json.load(fHandler)
    except FileNotFoundError:
        print(error_text(("Unable to find the file given by path: "
                          f"{PATH_TO_CONFIG_FILE}")))
        sys.exit(BROKEN_CONFIG_FILE_PATH)

    # Get the number of workers to interact with
    WORKER_COUNT: int = len(workerConf['workers'])

    _ans = 'n'
    while str.lower(_ans) in ['n', 'no']:
        _ans = input((f"{'Have' if WORKER_COUNT > 1 else 'Has'} the "
                      f"{WORKER_COUNT} "
                      f"{GE.plural_noun('worker', WORKER_COUNT)}"
                      " been started, yet? [y/n] ")).strip().lower()

    """ Creating the thread-shared objects
    """
    # Worker State Tracker Object
    obj_workerStateTracker: StateTracker = StateTracker(workerConf)

    _converter = {
        "RR": "Round-Robin",
        "LL": "Least-Loaded",
        "RANDOM": "Random"
    }

    # Worker updates handler object
    obj_jobUpdatesTracker: JobUpdateTracker = \
        JobUpdateTracker(_converter[TYPE_OF_SCHEDULING])

    # Job Request Handler Object
    obj_jobRequestHandler: JobRequestHandler = \
        JobRequestHandler(obj_jobUpdatesTracker)

    # ---
    # After this points we create the threads for the master
    # After this point any print statements need to acquire the
    # PRINT_LOCK before printing
    # ---

    """
     - Creating the various threads needed at the master machine and
     passing in the required parameters.
     - All the threads are declared as daemon threads.
     - Daemon threads are those threads which are killed when the main
     program exits.
    """
    jobRequestThread = threading.Thread(name=("Listen for Incoming Job"
                                              "Requests"),
                                        target=listenForJobRequests,
                                        args=(obj_jobRequestHandler,
                                              obj_jobUpdatesTracker))
    jobRequestThread.daemon = True
    jobRequestThread.start()

    taskDispatchThread = None
    if TYPE_OF_SCHEDULING == "RANDOM":
        taskDispatchThread = threading.Thread(name=("Job Dispatcher -"
                                                    "Random Scheduling"),
                                              target=RandomScheduler.
                                              jobDispatcher,
                                              args=(obj_jobRequestHandler,
                                                    obj_workerStateTracker))
    elif TYPE_OF_SCHEDULING == "RR":
        taskDispatchThread = threading.Thread(name=("Job Dispatcher -"
                                                    "Round-Robin Scheduling"),
                                              target=RoundRobinScheduler.
                                              jobDispatcher,
                                              args=(obj_jobRequestHandler,
                                                    obj_workerStateTracker,
                                                    WORKER_COUNT))
    elif TYPE_OF_SCHEDULING == "LL":
        taskDispatchThread = threading.Thread(name=("Job Dispatcher -"
                                                    "Least-Loaded Scheduling"),
                                              target=LeastLoadedScheduler.
                                              jobDispatcher,
                                              args=(obj_jobRequestHandler,
                                                    obj_workerStateTracker,
                                                    WORKER_COUNT))
    else:
        PRINT_LOCK.acquire()
        print(error_text("Invalid value entered for type of scheduling!"))
        PRINT_LOCK.release()
        sys.exit(1)

    taskDispatchThread.daemon = True
    taskDispatchThread.start()

    WORKER_UPDATES_PORT: int = 5001
    WORKER_UPDATES_ADDR: Tuple[str, int] = \
        (socket.gethostname(), WORKER_UPDATES_PORT)

    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as \
         worker_updates_socket:
        worker_updates_socket.setsockopt(socket.SOL_SOCKET,
                                         socket.SO_REUSEADDR, 1)
        # Bind the socket to the address tuple
        worker_updates_socket.bind(WORKER_UPDATES_ADDR)

        # Put the socket into listening mode
        worker_updates_socket.listen(WORKER_COUNT)
        PRINT_LOCK.acquire()
        print(info_text(("Listening to updates from the workers on port: "
                         f"{WORKER_UPDATES_PORT}")))
        PRINT_LOCK.release()

        # List to hold the threads listening to updates from the workers
        workerUpdateThreads: List[threading.Thread] = []

        # Loop until all the workers connect to the master
        for _ in range(WORKER_COUNT):
            # Establish connection with the requesting worker
            workerSocket, workerAddress = worker_updates_socket.accept()

            # Get the worker number from the newly connected worker
            WORKER_ID: str = workerSocket.recv(BUFFER_SIZE).decode()

            # Printing connection updates
            PRINT_LOCK.acquire()
            print(
                  info_text(f"Connected to worker ID: {WORKER_ID} at address:")
                  )
            print(f"IP Address: {workerAddress[0]}")
            print(f"Socket: {workerAddress[1]}")
            PRINT_LOCK.release()

            # Start a new thread and return its thread object
            _temp = threading.Thread(target=workerUpdates,
                                     name=(f"Worker-{WORKER_ID} Update "
                                           "Listener"),
                                     args=(workerSocket,
                                           obj_workerStateTracker,
                                           obj_jobUpdatesTracker))
            _temp.daemon = True
            _temp.start()

            # Store the thread object in a list
            workerUpdateThreads.append(_temp)

        print(f"{workerUpdateThreads=}")

    print("You have reached the bottom of the '__main__'")
    print(threading.enumerate())

    """ Wait for all the threads to finish
    """
    # Wait for the thread listening for incoming job requests to finish
    jobRequestThread.join()

    # Wait for the thread dispatching tasks to the worker to finish
    taskDispatchThread.join()

    # Wait for the threads listening for worker updates to finish
    for updateThread in workerUpdateThreads:
        updateThread.join()
