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
            "task_family": <("map"|"reduce")>,
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
        msg_dict["task_family"] = task_family
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
            "worker_id": <worker_id>,
            "job_id": <job_id>,
            "task_family": <("map"|"reduce")>,
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
        msg_dict["task_family"] = task_family
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
            "task_family": <("map"|"reduce")>,
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
        msg_dict["task_family"] = task_family
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
            "worker_id": <worker_id>,
            "job_id": <job_id>,
            "task_family": <("map"|"reduce")>,
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
        msg_dict["task_family"] = task_family
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

    @staticmethod
    def connectBackMessage(back_off_time, public_key):
        """
        The final JSON string will be as follows:

        ```json
        {
            "back_off_time": <Time_In_Seconds>,
            "public_key": <Public_key_for_key_sharing>
        }
        ```

        """
        msg_dict = {}
        msg_dict["back_off_time"] = back_off_time
        msg_dict["public_key"] = public_key.decode()
        return json.dumps(msg_dict)

    @staticmethod
    def connectBackResponse(worker_id, enc_pri_key):
        """
        The final JSON string will be as follows:

        ```json
        {
            "worker_id": <worker_id>,
            "enc_pri_key": <Encrypted_private_key_for_key_sharing>
        }
        ```

        """
        msg_dict = {}
        msg_dict["worker_id"] = worker_id
        msg_dict["enc_pri_key"] = enc_pri_key.decode()
        return json.dumps(msg_dict)


class messageToWorkerTaskType(TypedDict):
    """```messageToWorkerTaskType``` class is used to help in creating the
    *type hint* for the dictionary that will contain the
    **parsed JSON message** that is sent to the worker.

    This class is essentially the *type hint* for the ```"task"``` field of the
    **parsed JSON message** that is sent to the worker.
    """
    task_id: str
    duration: int


class messageToWorkerType(TypedDict):
    """```messageToWorkerType``` class is the *type hint* for the dictionary
    that will contain the **parsed JSON message** that is sent to the worker.
    """
    worker_id: int
    job_id: str
    task_family: str
    task: messageToWorkerTaskType


class messageToMasterTaskType(TypedDict):
    """```messageToMasterTaskType``` class is used to help in creating the
    *type hint* for the dictionary that will contain the
    **parsed JSON message** that is sent to the master.

    This class is essentially the *type hint* for the ```"task"``` field of the
    **parsed JSON message** that is sent to the master.
    """
    task_id: str
    start_time: float
    end_time: float


class messageToMasterType(TypedDict):
    """```messageToMasterType``` class is the *type hint* for the dictionary
    that will contain the **parsed JSON message** that is sent to the master.
    """
    worker_id: int
    job_ID: str
    task_family: str
    task: messageToMasterTaskType
