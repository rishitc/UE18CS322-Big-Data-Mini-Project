import time

from ..Communication.protocol import YACS_Protocol


class RandomScheduler:
    @staticmethod
    def jobDispatcher(requestHandler, workerStateTracker, WORKER_COUNT):
        while True:
            jobID_family_task = None
            _temp = 0  # Initially we begin at the first worker

            # Get a pending task
            requestHandler.LOCK.acquire()
            if not requestHandler.isEmpty():
                jobID_family_task = requestHandler.getWaitingTask()
            requestHandler.LOCK.release()

            # If there is a Task that needs to be executed
            if jobID_family_task is not None:
                # Initially we have not found a worker with a free slot
                workerFound = False

                while workerFound is False:  # Until a free worker is not found
                    workerStateTracker.LOCK.acquire()

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
                                        worker_ID=_temp
                                       ))
                        # Once a worker with a free slot is found then
                        # 1. We dispatch the job to the worker
                        # 2. Update its state
                        workerStateTracker.getWorkerSocket(_temp)\
                            .sendall(protocolMsg)
                        workerStateTracker.allocateSlot(_temp)
                    workerStateTracker.LOCK.release()

                    _temp += 1
                    _temp %= WORKER_COUNT

                    # Sleep for a second to allow for the workerStateTracker
                    # to be updated by the thread: workerUpdates
                    time.sleep(1)
