import json
from typing import TypedDict

# This lock is used to get access to print onto the standard output
from Locks.MasterPrintLock import master
from Locks.WorkerPrintLock import worker


class YACS_Protocol:
    @staticmethod
    def createMessageToWorker(job_ID, task_family, task_ID, duration,
                              worker_ID):
        """
        The final JSON string will be as follows:

        ```json
        {
            "worker_id": <worker_id>,
            "job_id": <job_id>,
            "task family": <("map"|"reduce")>,
            "task": {
                        "task_id": "<task_id>",
                        "duration": <in seconds>
                    }
        }
        ```

        """
        assert task_family in ["map", "reduce"], ("Task family name "
                                                  f"{task_family} is "
                                                  "incorrect!")

        msg_dict = {}
        msg_dict["worker_id"] = worker_ID
        msg_dict["job_id"] = job_ID
        msg_dict["task family"] = task_family
        msg_dict["task"] = {
                                "task_id": task_ID,
                                "duration": duration
                            }
        return json.dumps(msg_dict)

    @staticmethod
    def createMessageToMaster(job_ID, task_family, task_ID, start_time,
                              end_time, worker_ID):
        """
        The final JSON string will be as follows:

        ```json
        {
            "worker_id":<worker_id>,
            "job_id":<job_id>,
            "task family": <("map"|"reduce")>,
            "task": {
                        "task_id": "<task_id>",
                        "start_time": <arrival_time_of_task_at_Worker>,
                        "end_time": <end_time_of_task_in_Worker>,
                    }
        }
        ```

        """
        assert task_family in ["map", "reduce"], ("Task family name "
                                                  f"{task_family} is "
                                                  "incorrect!")

        msg_dict = {}
        msg_dict["worker_id"] = worker_ID
        msg_dict["job_id"] = job_ID
        msg_dict["task family"] = task_family
        msg_dict["task"] = {
                                "task_id": task_ID,
                                "start_time": start_time,
                                "end_time": end_time,
                            }

        return json.dumps(msg_dict)

    @staticmethod
    def prettyPrintMessageToWorker(job_ID, task_family, task_ID, duration,
                                   worker_ID):
        """
        The final JSON string will be as follows:

        ```json
        {
            "worker_id": <worker_id>,
            "job_id": <job_id>,
            "task family": <("map"|"reduce")>,
            "task": {
                        "task_id": "<task_id>",
                        "duration": <in seconds>
                    }
        }
        ```

        """
        assert task_family in ["map", "reduce"], ("Task family name "
                                                  f"{task_family} is "
                                                  "incorrect!")

        msg_dict = {}
        msg_dict["worker_id"] = worker_ID
        msg_dict["job_id"] = job_ID
        msg_dict["task family"] = task_family
        msg_dict["task"] = {
                                "task_id": task_ID,
                                "duration": duration
                            }

        master.PRINT_LOCK.acquire()
        worker.PRINT_LOCK.acquire()
        print(json.dumps(msg_dict, indent=4))
        worker.PRINT_LOCK.release()
        master.PRINT_LOCK.release()

    @staticmethod
    def prettyPrintMessageToMaster(job_ID, task_family, task_ID, start_time,
                                   end_time, worker_ID):
        """
        The final JSON string will be as follows:

        ```json
        {
            "worker_id":<worker_id>,
            "job_id":<job_id>,
            "task family": <("map"|"reduce")>,
            "task": {
                        "task_id": "<task_id>",
                        "start_time": <arrival_time_of_task_at_Worker>,
                        "end_time": <end_time_of_task_in_Worker>
                    }
        }
        ```

        """
        assert task_family in ["map", "reduce"], ("Task family name "
                                                  f"{task_family} is "
                                                  "incorrect!")

        msg_dict = {}
        msg_dict["worker_id"] = worker_ID
        msg_dict["job_id"] = job_ID
        msg_dict["task family"] = task_family
        msg_dict["task"] = {
                                "task_id": task_ID,
                                "start_time": start_time,
                                "end_time": end_time,
                            }

        master.PRINT_LOCK.acquire()
        worker.PRINT_LOCK.acquire()
        print(json.dumps(msg_dict, indent=4))
        worker.PRINT_LOCK.release()
        master.PRINT_LOCK.release()


class messageToWorkerTaskType(TypedDict):
    task_id: str
    duration: int
    worker_id: int


class messageToWorkerType(TypedDict):
    job_id: str
    task_family: str
    task: messageToWorkerTaskType


class messageToMasterTaskType(TypedDict):
    task_id: str
    start_time: float
    end_time: float


class messageToMasterType(TypedDict):
    worker_id: int
    job_ID: str
    task_family: str
    task: messageToMasterTaskType
