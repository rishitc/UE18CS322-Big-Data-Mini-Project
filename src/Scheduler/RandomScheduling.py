import random
import time
from typing import Set

from Communication.protocol import YACS_Protocol
from Scheduler.JobRequests import JobRequestHandler
from WorkerUtils.WorkerStateTracker import StateTracker


class RandomScheduler:
    @staticmethod
    def jobDispatcher(requestHandler: JobRequestHandler,
                      workerStateTracker: StateTracker):
        #  Initialize the random number generator.
        random.seed()
        workerIDsVisited: Set = set()

        while True:
            jobID_family_task = None

            # Get a pending task, if any
            requestHandler.LOCK.acquire()
            if not requestHandler.isEmpty():
                jobID_family_task = requestHandler.getWaitingTask()
            requestHandler.LOCK.release()

            # If there is a Task that needs to be executed
            if jobID_family_task is not None:
                # Initially we have not visited any worker
                workerIDsVisited.clear()

                # Initially we have not found a worker with a free slot
                workerFound = False

                while workerFound is False:  # Until a free worker is not found
                    workerStateTracker.LOCK.acquire()

                    # Pick a worker at random
                    _temp = random.choice(workerStateTracker.workerIDs)
                    workerIDsVisited.add(_temp)

                    # If the worker has a free slot
                    if workerStateTracker.isWorkerFree(_temp):
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
                                        # We only get _temp in the LOCK
                                        # i.e. critical section
                                        worker_ID=_temp
                                        ))
                        # Once a worker with a free slot is found then
                        # 1. We dispatch the job to the worker
                        # 2. Update its state
                        workerStateTracker.getWorkerSocket(_temp)\
                            .sendall(protocolMsg)
                        workerStateTracker.allocateSlot(_temp)

                        # We have found a worker and hence set this to True
                        workerFound = True

                    workerStateTracker.LOCK.release()

                    # In the case where none of the workers have a free slot
                    if list(workerIDsVisited) == workerStateTracker.workerIDs:
                        # Sleep for a second to allow for the
                        # workerStateTracker to be updated by the
                        # thread: workerUpdates
                        time.sleep(1)

                        # Clear the worker IDs visited set as we are
                        # restarting our search for a free slot on one of the
                        # workers
                        workerIDsVisited.clear()
