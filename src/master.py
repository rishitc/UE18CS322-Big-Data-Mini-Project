import json
import socket
import sys
import threading
import time
from typing import List, Optional, Tuple
import colored as TC
from colored.colored import attr
import inflect
from cryptography.fernet import Fernet

# This lock is used to get access to print onto the standard output
from Locks.MasterPrintLock import master

from MasterUtils.WorkerStateTracker import StateTracker
from UpdateTracker.JobUpdateTracker import Tracker as JobUpdateTracker

from Scheduler.JobRequests import JobRequestHandler
from Scheduler.RandomScheduling import RandomScheduler
from Scheduler.RoundRobinScheduling import RoundRobinScheduler
from Scheduler.LeastLoadedScheduling import LeastLoadedScheduler

from Communication.protocol import messageToMasterType


# The maximum amount of data to be received at once is specified by BUFFER_SIZE
BUFFER_SIZE: int = 4096

# Error codes to return to the shell
# The Unix programs' style for error codes has
# been used here
MISSING_CMD_LINE_ARGS: int = 2
BROKEN_CONFIG_FILE_PATH: int = 1

GE = inflect.engine()  # GE means Grammar Engine


def info_text(text):
    """```info_text``` returns a modified version of the input ```text``` such
    that it looks like an *information message* when printed on the CLI.

    **param** ```text```: The input string that will be modified to look like
    an *information message* when printed on the CLI

    **type** ```text```: str

    **return**: The modified version of the input ```text``` such
    that it looks like an *information message* when printed on the CLI

    **rtype**: str
    """
    return f"{TC.fg(6) + TC.attr(1)}INFO:{TC.attr(0)} {text}"


def error_text(text):
    """```error_text``` returns a modified version of the input ```text``` such
    that it looks like an *error message* when printed on the CLI.

    **param** ```text```: The input string that will be modified to look like
    an *error message* when printed on the CLI

    **type** ```text```: str

    **return**: The modified version of the input ```text``` such
    that it looks like an *error message* when printed on the CLI

    **rtype**: str
    """
    return f"{TC.fg(1) + TC.attr(1)}ERROR:{TC.attr(0)} {text}"


def success_text(text):
    """```success_text``` returns a modified version of the input ```text```
    such that it looks like a *success message* when printed on the CLI.

    **param** ```text```: The input string that will be modified to look like
    a *success message* when printed on the CLI

    **type** ```text```: str

    **return**: The modified version of the input ```text``` such
    that it looks like a *success message* when printed on the CLI

    **rtype**: str
    """
    return f"{TC.fg(2) + TC.attr(1)}SUCCESS:{TC.attr(0)} {text}"


def checkJobPoller(jobRequestHandler: JobRequestHandler,
                   jobUpdateTracker: JobUpdateTracker,
                   job_id: str):
    """```checkJobPoller``` continuously checks if all the tasks, for
    the pending job given by ```job_id```, have been dispatched to one
    or the other worker, by the master. It also checks whether the
    updates from the workers, for every dispatched task, of the running
    job given by ```job_id```, have been received by the master.

    It prints a ```success message``` once all tasks of all the pending jobs
    have been dispatched as well as once all the tasks' updates for all jobs
    have been received, by the master.

    **param** ```jobRequestHandler```: Used to track the task dispatch status
    of the job

    **type** ```jobRequestHandler```: JobRequestHandler

    **param** ```jobUpdateTracker```: Used to track the updates from the
    workers about the tasks assigned belonging to the different jobs

    **type** ```jobUpdateTracker```: JobUpdateTracker
    """
    isJobDispatchComplete = {}
    _isPrint_1: bool = False
    isJobUpdatesComplete = {}
    _isPrint_2: bool = False

    while (isJobDispatchComplete is not None) or \
          (isJobUpdatesComplete is not None):
        jobRequestHandler.LOCK.acquire()
        isJobDispatchComplete = jobRequestHandler.jobRequests.get(job_id)
        jobRequestHandler.LOCK.release()

        if (isJobDispatchComplete is None) and (not _isPrint_1):
            master.PRINT_LOCK.acquire()
            print(success_text((f"All tasks of job-{job_id} have been "
                                "dispatched to the workers!"))
                  )
            master.PRINT_LOCK.release()
            _isPrint_1 = True

        jobUpdateTracker.LOCK.acquire()
        isJobUpdatesComplete = jobUpdateTracker.jobs_time.get(job_id)
        jobUpdateTracker.LOCK.release()

        if (isJobUpdatesComplete is None) and (not _isPrint_2):
            master.PRINT_LOCK.acquire()
            print(success_text((f"All task updates of job-{job_id} have been"
                                " received!")))
            master.PRINT_LOCK.release()
            _isPrint_2 = True

        time.sleep(0.01)


def listenForJobRequests(jobRequestHandler: JobRequestHandler,
                         jobUpdateTracker: JobUpdateTracker):
    """```listenForJobRequests``` listens for new job requests from the client
    code.

    **param** ```jobRequestHandler```: Used to track the task dispatch status
    of the job

    **type** ```jobRequestHandler```: JobRequestHandler

    **param** ```jobUpdateTracker```: Used to track the updates from the
    workers about the tasks assigned belonging to the different jobs

    **type** ```jobUpdateTracker```: JobUpdateTracker
    """
    _JOB_REQUEST_ADDR: Tuple[str, int] = ("localhost", 5000)
    # Older version of address tuple used: (socket.gethostname(), 5000)

    master.PRINT_LOCK.acquire()
    print(info_text("Inside listenForJobRequests"))
    master.PRINT_LOCK.release()

    # Setup the master socket to listen for job requests
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as jobReqSocket:
        jobReqSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        jobReqSocket.bind(_JOB_REQUEST_ADDR)
        while True:
            master.PRINT_LOCK.acquire()
            print(info_text("Listening for incoming job requests"))
            master.PRINT_LOCK.release()
            jobReqSocket.listen()
            clientConn, clientAddr = jobReqSocket.accept()

            master.PRINT_LOCK.acquire()
            print(info_text("Connected to client at address:"))
            print(f"IP Address: {clientAddr[0]}")
            print(f"Socket: {clientAddr[1]}")
            master.PRINT_LOCK.release()

            # while True:
            jobRequest = clientConn.recv(BUFFER_SIZE)
            if not jobRequest:
                clientConn.close()
                break

            # Decode and parse the JSON string
            parsedJSON_Msg = json.loads(jobRequest.decode())
            _recv_job_id: str = parsedJSON_Msg["job_id"]

            # Add new job request to job request handler object
            # for task dispatch
            # print("Acquiring jobRequestHandler LOCK")
            jobRequestHandler.LOCK.acquire()
            jobRequestHandler.addJobRequest(parsedJSON_Msg)
            jobRequestHandler.LOCK.release()
            # print("Releasing jobRequestHandler LOCK")

            # Add new job request to job request handler object
            # for tracking dispatched tasks' completion by the
            # workers
            # print("Acquiring jobUpdateTracker LOCK")
            jobUpdateTracker.LOCK.acquire()
            jobUpdateTracker.addJobRequest(parsedJSON_Msg)
            jobUpdateTracker.LOCK.release()
            # print("Releasing jobUpdateTracker LOCK")

            jobRequestHandler.LOCK.acquire()
            _state = jobRequestHandler.jobRequests
            jobRequestHandler.LOCK.release()
            master.PRINT_LOCK.acquire()
            print(f"jobRequestHandler.jobRequests={_state}")
            master.PRINT_LOCK.release()

            # Close the client connection as we have finished receiving the job
            # request from the client
            clientConn.close()

            _job_poller_thread = threading.Thread(name="Job Poller Thread",
                                                  target=checkJobPoller,
                                                  args=(jobRequestHandler,
                                                        jobUpdateTracker,
                                                        _recv_job_id)
                                                  )
            _job_poller_thread.daemon = True
            _job_poller_thread.start()

            master.PRINT_LOCK.acquire()
            print(info_text("Created the job poller thread!"))
            print("You have reached the bottom of the '__main__'")
            print(threading.enumerate())
            master.PRINT_LOCK.release()

            # _job_poller_thread.join()


def workerUpdates(workerSocket: socket.socket,
                  workerStateTracker: StateTracker,
                  jobUpdateTracker: JobUpdateTracker,
                  WORKER_KEY):
    """```workerUpdates``` captures the updates from the worker as and when
    they complete the tasks assigned to them, and respond back.

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
    dec_obj = Fernet(WORKER_KEY)
    while True:
        workerUpdate: str = workerSocket.recv(BUFFER_SIZE).decode()
        if not workerUpdate:
            workerSocket.close()
            break

        _temp: str = ''
        for i in workerUpdate.split('==')[:-1]:
            _temp += dec_obj.decrypt((i + '==').encode()).decode()
        workerUpdate = _temp

        # Preprocess the received JSON data. This helps prevent
        # JSON parsing errors when more then one message has been
        # received at once at the master
        workerUpdate = "[" + workerUpdate.replace("}{", "},{") + "]"

        master.PRINT_LOCK.acquire()
        print(f"Received worker update at master: {workerUpdate}")
        master.PRINT_LOCK.release()

        parsedJSON_Msg: List[messageToMasterType] = \
            json.loads(workerUpdate)

        msg: messageToMasterType
        for msg in parsedJSON_Msg:
            jobUpdateTracker.LOCK.acquire()
            jobUpdateTracker.updateJob(msg)
            jobUpdateTracker.LOCK.release()

            workerStateTracker.LOCK.acquire()
            workerStateTracker.freeSlot(msg["worker_id"])
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

    """ Creating the thread-shared objects.
    """
    # Worker State Tracker Object
    obj_workerStateTracker: StateTracker = StateTracker(workerConf)

    _converter = {
        "RR": "Round-Robin",
        "LL": "Least-Loaded",
        "RANDOM": "Random"
    }

    # Worker updates handler object
    print("JobUpdateTracker Initialized")
    obj_jobUpdatesTracker: JobUpdateTracker = \
        JobUpdateTracker(_converter[TYPE_OF_SCHEDULING])

    # Job Request Handler Object
    obj_jobRequestHandler: JobRequestHandler = \
        JobRequestHandler(obj_jobUpdatesTracker)

    # ---
    # After this points we create the threads for the master
    # After this point any print statements need to acquire the
    # master.PRINT_LOCK before printing
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
                                                    obj_workerStateTracker))
    else:
        master.PRINT_LOCK.acquire()
        print(error_text("Invalid value entered for type of scheduling!"))
        master.PRINT_LOCK.release()
        sys.exit(1)

    master.PRINT_LOCK.acquire()
    print(info_text((f"Selected scheduling algorithm: {attr(1)}"
                     f"{_converter[TYPE_OF_SCHEDULING]}{attr(0)}")))
    master.PRINT_LOCK.release()

    taskDispatchThread.daemon = True
    taskDispatchThread.start()

    # Worker connect back mechanism
    PUBLIC_KEY = Fernet.generate_key()
    PUBLIC_KEY_OBJ = Fernet(PUBLIC_KEY)

    obj_workerStateTracker.LOCK.acquire()
    obj_workerStateTracker.connectBackRequest(PUBLIC_KEY)
    obj_workerStateTracker.LOCK.release()

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
        master.PRINT_LOCK.acquire()
        print(info_text(("Listening to updates from the workers on port: "
                         f"{WORKER_UPDATES_PORT}")))
        master.PRINT_LOCK.release()

        # List to hold the threads listening to updates from the workers
        workerUpdateThreads: List[threading.Thread] = []

        # Loop until all the workers connect to the master
        for _ in range(WORKER_COUNT):
            # Establish connection with the requesting worker
            workerSocket, workerAddress = worker_updates_socket.accept()

            # Get the worker number from the newly connected worker
            response_msg = json.loads(workerSocket.recv(BUFFER_SIZE).decode())
            response_msg["enc_pri_key"] = response_msg["enc_pri_key"].encode()
            WORKER_ID: str = response_msg["worker_id"]
            _worker_key = PUBLIC_KEY_OBJ.decrypt(response_msg["enc_pri_key"])

            obj_workerStateTracker.LOCK.acquire()
            obj_workerStateTracker.workerState[int(WORKER_ID)]["pri_key"] = \
                _worker_key
            obj_workerStateTracker.LOCK.release()

            # Printing connection updates
            master.PRINT_LOCK.acquire()
            print(
                  info_text(f"Connected to worker ID: {WORKER_ID} at address:")
                  )
            print(f"IP Address: {workerAddress[0]}")
            print(f"Socket: {workerAddress[1]}")
            print(f"Private Key: {_worker_key}")
            master.PRINT_LOCK.release()

            # Start a new thread and return its thread object
            _temp = threading.Thread(target=workerUpdates,
                                     name=(f"Worker-{WORKER_ID} Update "
                                           "Listener"),
                                     args=(workerSocket,
                                           obj_workerStateTracker,
                                           obj_jobUpdatesTracker,
                                           _worker_key))
            _temp.daemon = True
            _temp.start()

            # Store the thread object in a list
            workerUpdateThreads.append(_temp)

        master.PRINT_LOCK.acquire()
        print(f"{workerUpdateThreads=}")
        master.PRINT_LOCK.release()

    master.PRINT_LOCK.acquire()
    print("You have reached the bottom of the '__main__'")
    print(threading.enumerate())
    master.PRINT_LOCK.release()

    """ Wait for all the threads to finish.
    """
    # Wait for the thread listening for incoming job requests to finish
    jobRequestThread.join()

    # Wait for the thread dispatching tasks to the worker to finish
    taskDispatchThread.join()

    # Wait for the threads listening for worker updates to finish
    for updateThread in workerUpdateThreads:
        updateThread.join()
