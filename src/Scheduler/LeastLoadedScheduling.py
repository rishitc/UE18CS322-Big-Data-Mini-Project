import time
from typing import Optional

from Communication.protocol import YACS_Protocol
from Scheduler.JobRequests import JobRequestHandler
from WorkerUtils.WorkerStateTracker import StateTracker


class LeastLoadedScheduler:
    """ The ```LeastLoadedScheduler``` class implements the **Least-Loaded
    Scheduling** algorithm. In this algorithm the Master looks at the state
    of all the machines and checks which machine has most number of free
    slots. It then launches the task on that machine. If none of the machines
    have free slots available, the Master waits for 1 second and repeats the
    process. This process continues until a free slot is found.
    """
    @staticmethod
    def jobDispatcher(requestHandler: JobRequestHandler,
                      workerStateTracker: StateTracker):
        """```jobDispatcher``` implements the **Least-Loaded Scheduling**
        algorithm

        **param** ```requestHandler```: This object will track the tasks of
        incomplete jobs, and provide them for allocation, respecting the
        *map-reduce* dependency

        **type** ```requestHandler```: JobRequestHandler

        **param** ```workerStateTracker```: This object will track and update
        how loaded the workers are, i.e. how many free slots fo they have

        **type** ```workerStateTracker```: StateTracker
        """
        while True:
            jobID_family_task = None

            # Get a pending task if any
            requestHandler.LOCK.acquire()
            if not requestHandler.isEmpty():
                jobID_family_task = requestHandler.getWaitingTask()
            requestHandler.LOCK.release()

            # If there is a Task that needs to be executed
            if jobID_family_task is not None:
                # Initially we have not found a worker with a free slot
                workerFound: bool = False

                while workerFound is False:  # Until a free worker is not found
                    workerStateTracker.LOCK.acquire()

                    # Get the least loaded worker if present, else None
                    _temp: Optional[int] = workerStateTracker\
                        .getLeastLoadedWorkerID()

                    # If a least loaded worker is found
                    if _temp is not None:
                        workerFound = True  # We have found a worker

                        # Create the JSON protocol message
                        protocolMsg = (YACS_Protocol
                                       .createMessageToWorker
                                       (
                                        job_ID=jobID_family_task[0],
                                        task_family=jobID_family_task[1],
                                        task_ID=(jobID_family_task[2]
                                                 ["task_id"]),
                                        duration=(jobID_family_task[2]
                                                  ["duration"]),
                                        worker_ID=_temp
                                        ))
                        # Once a worker with a free slot is found then
                        # 1. We dispatch the job to the worker
                        # 2. Update its state
                        workerStateTracker.getWorkerSocket(_temp)\
                            .sendall(protocolMsg.encode())
                        workerStateTracker.allocateSlot(_temp)

                    workerStateTracker.LOCK.release()

                    # If none of the machines have free slots available,
                    # then the Master waits for 1 second and repeats the
                    # process
                    if workerFound is False:
                        # Sleep for 1 second to allow for the
                        # workerStateTracker to be updated by
                        # the thread: workerUpdates
                        time.sleep(1)
                    else:
                        # After sending a task to the worker, sleep for 0.01s
                        # seconds before sending the next task. This done so
                        # that the worker buffer only has at most 1 task in
                        # its socket's buffer
                        time.sleep(0.01)
