class JobRequestHandler:
    """This class stores the incoming job requests from the job request
     port. The incoming jobs are stored with a certain priority; at the
     moment First Come First Served technique is used. It also provides
     waiting tasks for the highest priority job request,
     in order of map tasks then reduce tasks.

    Once a job has been completely allocated to one or the worker. Its entry
     is removed from this object.
    """
    def __init__(self):
        self.jobRequests = {}
        self.priorityOrder = []

    def addJobRequest(self, requestSpecs):
        """Adds the request specification to the objects
         jobRequests dictionary and adds the job ID to the
         priorityOrder list as per the priority order of the
         job.

        :param requestSpecs: Dictionary got after converting the incoming
         JSON request string into a dictionary
        :type requestSpecs: dict
        """
        _JOB_ID: int = requestSpecs["job_id"]
        self.jobRequests[_JOB_ID] = {
            "map": requestSpecs["map_tasks"],
            "reduce": requestSpecs["reduce_tasks"]
        }
        self.priorityOrder.append(requestSpecs["job_id"])

    def getWaitingTask(self):
        assert len(self.priorityOrder) > 0, f"No job requests exist!"

        _JOB_ID = self.priorityOrder[0]
        _SELECTED_TASK = None

        # Check for a pending map task
        if self.jobRequests[_JOB_ID]["map"]:
            _SELECTED_TASK = self.jobRequests[_JOB_ID]["map"].pop(0)

        # Check for a pending reduce task
        else:
            _SELECTED_TASK = self.jobRequests[_JOB_ID]["reduce"].pop(0)

        # Check if this task is the last task
        if (not self.jobRequests[_JOB_ID]["map"]) and \
           (not self.jobRequests[_JOB_ID]["reduce"]):
            del self.jobRequests[_JOB_ID]
            self.priorityOrder.remove(_JOB_ID)

        return (_JOB_ID, _SELECTED_TASK)

    def isEmpty(self):
        return True if not self.priorityOrder else False
