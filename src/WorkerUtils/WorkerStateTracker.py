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
            print(f"{worker['worker_id']=}")
            self.workerState[worker["worker_id"]] = {
                "slots": worker["slots"],
                "port": worker["port"],
                "free slots": worker["slots"],
            }

    def isWorkerFree(self, workerID: int, demand: int = 1) -> bool:
        """Check if the worker whose ```worker_id``` key is equal to
        workerID.

        :param workerID: ```worker_id``` value of the worker node we checking
        for free slots
        :type workerID: int
        :param demand: Specifies the number of free slots we are looking
        for in the worker node with ```worker_id``` equal to workerID, defaults
        to 1
        :type demand: int, optional
        """
        return True if self.workerState[workerID]["free slots"] >= demand \
            else False

    def showWorkerStates(self) -> None:
        print(f"{self.workerState=}")
