import socket
from threading import Lock
from typing import List, Optional

from Communication.protocol import YACS_Protocol
# from Locks.MasterPrintLock import master


class StateTracker:
    def __init__(self, confObj: dict) -> None:
        """Store the list of the worker dictionaries in a new dictionary
         indexed using the ```worker_id``` as key.

        **param** ```configObj```: Dictionary got from loading in the json
        data stored in the worker configuration file

        **type** ```configObj```: dict
        """
        self.workerState = {}
        self.workerIDs: List[int] = []
        self.LOCK = Lock()

        for worker in confObj["workers"]:
            # master.PRINT_LOCK.acquire()
            # print(f"{worker['worker_id']=}")
            # master.PRINT_LOCK.release()

            workerConnSocket = socket.socket(socket.AF_INET,
                                             socket.SOCK_STREAM)
            workerConnSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                        1)
            # master.PRINT_LOCK.acquire()
            # print(f'{worker["port"]=}')
            # master.PRINT_LOCK.release()

            workerConnSocket.connect((socket.gethostname(), worker["port"]))
            self.workerState[worker["worker_id"]] = {
                "slots": worker["slots"],
                "port": worker["port"],
                "free slots": worker["slots"],
                "socket": workerConnSocket
            }
            self.workerIDs.append(worker["worker_id"])

        # Sort the workerIDs
        self.workerIDs.sort()

    def isWorkerFree(self, workerID: int, demand: int = 1) -> bool:
        """```isWorkerFree``` checks if the worker whose ```worker_id``` key
        is equal to ```workerID```, has ```demand``` number of free slots or
        not. By default ```demand``` is set to 1.

        **param** ```workerID```: ```worker_id``` value of the worker node
        we are checking for free slots

        **type** ```workerID```: int

        **param** ```demand```: Specifies the number of free slots we are
        looking for in the worker node with ```worker_id``` equal to workerID,
        defaults to 1

        **type** ```demand```: int, optional

        **return**: Returns True if the number of free slots given by
        ```demand``` are found, else it returns false

        **rtype**: bool
        """
        # master.PRINT_LOCK.acquire()
        # print(f"{workerID=}")
        # print(f"{workerID in self.workerIDs}")
        # master.PRINT_LOCK.release()

        return True if self.workerState[workerID]["free slots"] >= demand \
            else False

    def showWorkerStates(self) -> None:
        """```showWorkerStates``` displays the contents of the workerState dictionary
        onto the standard output (here, CLI), for *debugging purposes*.
        """
        print(f"{self.workerState=}")

    def getWorkerSocket(self, workerID: int) -> socket.socket:
        """```getWorkerSocket``` returns the socket which is used to send tasks to
        the worker with ID ```workerID```.

        **param** ```workerID```: ID of the worker for whom the socket is
        desired

        **type** ```workerID```: int

        **return** The socket which is used to send tasks to
        the worker with ID ```workerID```

        **rtype** socket.socket
        """
        return self.workerState[workerID]["socket"]

    def allocateSlot(self, workerID: int, task_count: int = 1) -> None:
        """```allocateSlot``` allocates the task to the worker and decrements
        the number of free slots in that worker.

        **param** ```workerID```: Specifies the worker to which we are
        allocating the task to

        **type** ```workerID```: int

        **param** ```task_count```: Specifies the number of tasks being
        allocated the worker, defaults to 1

        **type** ```task_count```: int, optional
        """
        assert self.isWorkerFree(workerID, task_count) is True,\
            "Over allocating tasks to worker!"
        self.workerState[workerID]["free slots"] -= task_count

    def freeSlot(self, workerID: int, task_count: int = 1) -> None:
        """```freeSlot``` updates the state of the worker to indicate task completion
        by incrementing the number of free slots on that worker.

        **param** ```workerID```: Specifies the worker which has completed its
        task

        **type** ```workerID```: int

        **param** ```task_count```: Specifies the number of tasks compelted by
        the worker, defaults to 1

        **type** ```task_count```: int, optional
        """
        assert self.workerState[workerID]["free slots"] != \
            self.workerState[workerID]["slots"],\
            "There are no slots to free up!"
        self.workerState[workerID]["free slots"] += task_count

    def getLeastLoadedWorkerID(self) -> Optional[int]:
        """```getLeastLoadedWorkerID``` this methods check all the worker
        states and returns the worker ID of the **least loaded worker**. In the
        case where there are **no workers with free slots**, then it returns
        ```None```.

        **return**: Worker ID of the least loaded worker or ```None``` if all
        the workers are **fully loaded**

        **rtype**: Optional[int]
        """
        # Variables used to track the least loaded worker
        _least_loaded_workerID = None
        _least_loaded_workerFreeSlots = 0

        for workerID in self.workerIDs:
            # Get the free slots of worker with ID: workerID
            _free_slot_count = self.workerState[workerID]["free slots"]

            if _free_slot_count > _least_loaded_workerFreeSlots:
                # If the worker with ID: workerID has more free slots
                # then update the tracking variables
                _least_loaded_workerID = workerID
                _least_loaded_workerFreeSlots = _free_slot_count

        return _least_loaded_workerID

    def connectBackRequest(self, public_key):
        """```connectBackRequest``` is used to send a message to all the workers on
        their *socket for receiving tasks from the master* with the public key
        information as well as the time after which the individual worker
        should attempt to connect back to the master.

        **param** ```public_key```: This is the encryption key which is shared
        with the worker so that they can encrypt their private keys and later
        send it back to the master, in encrypted format using this public key

        **type** ```public_key```: bytes
        """
        back_off_time = 0.5
        for workerID in self.workerIDs:
            message = YACS_Protocol \
                .connectBackMessage(back_off_time=back_off_time,
                                    public_key=public_key)
            self.workerState[workerID]["socket"].sendall(message.encode())

            back_off_time += 0.5

    def __del__(self):
        """```__del__``` closes all task dispatch sockets to the workers.
        """
        for workerID in self.workerIDs:
            self.workerState[workerID]["socket"].close()
