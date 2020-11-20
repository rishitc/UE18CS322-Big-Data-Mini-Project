import socket


class StateTracker:
    def __init__(self, confObj: dict) -> None:
        """Store the list of the worker dictionaries in a new dictionary
         indexed by the ```worker_id``` key

        :param configObj: Dictionary got from loading in the json
         data stored in the worker configuration file
        :type configObj: dict
        """
        self.workerState = {}

        for worker in confObj["workers"]:
            # print(f"{worker['worker_id']=}")
            workerConnSocket = socket.socket(socket.AF_INET,
                                             socket.SOCK_STREAM)
            workerConnSocket.connect((socket.gethostname(), worker["port"]))
            self.workerState[worker["worker_id"]] = {
                "slots": worker["slots"],
                "port": worker["port"],
                "free slots": worker["slots"],
                "socket": workerConnSocket
            }

    def isWorkerFree(self, workerID: int, demand: int = 1) -> bool:
        """Check if the worker whose ```worker_id``` key is equal to
         workerID.

        :param workerID: ```worker_id``` value of the worker node we are
         checking for free slots
        :type workerID: int
        :param demand: Specifies the number of free slots we are looking
         for in the worker node with ```worker_id``` equal to workerID,
         defaults to 1
        :type demand: int, optional
        :return: Returns True if the number of free slots given by ```demand```
         are found, else it returns false
        :rtype: bool
        """
        return True if self.workerState[workerID]["free slots"] >= demand \
            else False

    def showWorkerStates(self) -> None:
        print(f"{self.workerState=}")

    def allocateSlot(self, workerID: int, task_count: int = 1) -> None:
        """Allocates the task to the worker and decrements the number of
         free slots in that worker

        :param workerID: Specifies the worker to which we are allocating the
         task to
        :type workerID: int
        :param task_count: Specifies the number of tasks being allocated the
         worker, defaults to 1
        :type task_count: int, optional
        """
        assert self.isWorkerFree(workerID, task_count) is True,\
            "Over allocating tasks to worker!"
        self.workerState[workerID]["free slots"] -= task_count

    def freeSlot(self, workerID: int, task_count: int = 1) -> None:
        """Updates the state of the worker to indicate task completion
         by incrementing the number of free slots on that worker

        :param workerID: Specifies the worker which has completed its task
        :type workerID: int
        :param task_count: Specifies the number of tasks compelted by the
         worker, defaults to 1
        :type task_count: int, optional
        """
        assert self.workerState[workerID]["free slots"] != \
            self.workerState[workerID]["slots"],\
            "There are no slots to free up!"
        self.workerState[workerID]["free slots"] += task_count
