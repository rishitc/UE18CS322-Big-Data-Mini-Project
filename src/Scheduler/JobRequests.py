from threading import Lock
from typing import Optional, Tuple

from UpdateTracker.JobUpdateTracker import Tracker as JobUpdateTracker


class JobRequestHandler:
    """
    This class stores the *incoming job requests* from the job request
    port.

    Once a job has been completely allocated, i.e. all its map and reduced
    tasks have been dispatched to one or the other worker, then its entry
    is removed from this object.
    """
    def __init__(self, workerUpdatesTracker: JobUpdateTracker):
        self.jobRequests = {}
        # self.priorityOrder = []
        self.LOCK = Lock()
        self.workerUpdatesTracker: JobUpdateTracker = workerUpdatesTracker

    def addJobRequest(self, requestSpecs):
        """
        ```addJobRequest``` adds the job request's specification to
        the handler object's ```jobRequests``` dictionary.

        **param** ```requestSpecs```: Dictionary got after converting the
        incoming JSON request string into a dictionary

        **type** ```requestSpecs```: dict
        """
        _JOB_ID: int = requestSpecs["job_id"]
        self.jobRequests[_JOB_ID] = {
            "map": requestSpecs["map_tasks"],
            "reduce": requestSpecs["reduce_tasks"]
        }
        # self.priorityOrder.append(requestSpecs["job_id"])

    def getWaitingTask(self) -> Optional[Tuple[Optional[int],
                                               Optional[str],
                                               Optional[dict]]]:
        """```getWaitingTask``` returns a task to be allocated to one of the
        workers for execution as well as the task's related meta-data.

        ## Algorithm:
        ```
        1. For every job in the jobRequests list:
            1.1 Check if the job has any pending map tasks
                1.1.1 Return any map task of the job and associated meta-data
            1.2 else
                1.2.1 Check if all the job's map tasks have completed
                    1.2.1.1 Return any reduce task of the job and associated
                            meta-data
                1.2.2 else
                    1.2.2.1 Continue and hence check the next pending job
        2. Return None as there is no assignable task available
        ```

        **return** Task meta-data and the task-dictionary
        **rtype** Optional[Tuple[Optional[int], Optional[str], Optional[dict]]]
        """
        # If there are no pending tasks and hence no pending jobs
        # then return None
        if len(self.jobRequests) == 0:
            return None

        _JOB_ID: Optional[int] = None
        _SELECTED_TASK: Optional[dict] = None
        _TASK_TYPE: Optional[str] = None

        for jobID in self.jobRequests:
            # Check for a pending map task
            if self.jobRequests[jobID]["map"]:
                _SELECTED_TASK = self.jobRequests[jobID]["map"].pop(0)
                _TASK_TYPE = "map"
                _JOB_ID = jobID

                # Exit the loop as we have found a suitable task
                break

            else:  # Check for pending reduce tasks, if any
                self.workerUpdatesTracker.LOCK.acquire()
                _temp = self.workerUpdatesTracker.isMapComplete(jobID)
                self.workerUpdatesTracker.LOCK.release()

                # if jobID:
                #   print(f"Have all map tasks completed {_temp} for {jobID}")

                if _temp:  # If the map tasks of the job have completed
                    if self.jobRequests[jobID]["reduce"]:
                        # Check for a pending reduce task
                        _SELECTED_TASK = self.jobRequests[jobID]["reduce"]\
                            .pop(0)
                        # print(f"{_SELECTED_TASK=}")
                        _TASK_TYPE = "reduce"
                        _JOB_ID = jobID

                        # Exit the loop as we have found a suitable task
                        break

        if (_SELECTED_TASK is None) and (_JOB_ID is None) and\
           (_TASK_TYPE is None):
            return None

        # Check if this task is the last task, if so then remove its
        # entry from this object's state
        if (not self.jobRequests[_JOB_ID]["map"]) and \
           (not self.jobRequests[_JOB_ID]["reduce"]):
            del self.jobRequests[_JOB_ID]
            # self.priorityOrder.remove(_JOB_ID)

        print("Selected tuple:", (_JOB_ID, _TASK_TYPE, _SELECTED_TASK))
        return (_JOB_ID, _TASK_TYPE, _SELECTED_TASK)

    def isEmpty(self) -> bool:
        """```isEmpty``` checks if the ```jobRequests``` dictionary is
        of the handler is empty.

        **return** Return True if the ```jobRequests``` dictionary is
        empty else it returns False
        **rtype** bool
        """
        return not self.jobRequests
