import socket
from threading import Lock
from typing import List, Optional


class StateTracker:
    def __init__(self, confObj: dict) -> None:
        """Store the list of the worker dictionaries in a new dictionary
         indexed by the ```worker_id``` key.

        **param** ```configObj```: Dictionary got from loading in the json
        data stored in the worker configuration file

        **type** ```configObj```: dict
        """
        self.workerState = {}
        self.workerIDs: List[int] = []
        self.LOCK = Lock()

        for worker in confObj["workers"]:
            # print(f"{worker['worker_id']=}")
            workerConnSocket = socket.socket(socket.AF_INET,
                                             socket.SOCK_STREAM)
            workerConnSocket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,
                                        1)
            # print(f'{worker["port"]=}')
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
        """Checks if the worker whose ```worker_id``` key is equal to
         ```workerID```, has ```demand``` number of free slots or not.
         By default ```demand``` is set to 1.

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
        # print(f"{workerID=}")
        # print(f"{workerID in self.workerIDs}")
        return True if self.workerState[workerID]["free slots"] >= demand \
            else False

    def showWorkerStates(self) -> None:
        print(f"{self.workerState=}")

    def getWorkerSocket(self, workerID):
        return self.workerState[workerID]["socket"]

    def allocateSlot(self, workerID: int, task_count: int = 1) -> None:
        """Allocates the task to the worker and decrements the number of
         free slots in that worker.

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
        """Updates the state of the worker to indicate task completion
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

    def __del__(self):
        """```__del__``` Closes all task dispatch sockets to the workers.
        """
        for workerID in self.workerIDs:
            self.workerState[workerID]["socket"].close()
