import json


class YACS_Protocol:
    @staticmethod
    def createMessageToWorker(job_ID, task_family, task_ID, duration,
                              worker_ID):
        """
        The final JSON string will be as follows:
        {
            "worker_id": <worker_id>,
            "job_id": <job_id>,
            "task family": <("map_tasks"|"reduce_tasks")>,
            "task":[
                    {
                        "task_id": "<task_id>",
                        "duration": <in seconds>
                    },
                    ]
        }
        """
        msg_dict = {}
        msg_dict["worker_id"] = worker_ID
        msg_dict["job_id"] = job_ID
        msg_dict["task family"] = task_family
        msg_dict["task"] = [
                            {
                                "task_id": task_ID,
                                "duration": duration
                            }
                            ]
        return json.dumps(msg_dict)

    @staticmethod
    def createMessageToMaster(job_ID, task_family, task_ID, start_time,
                              end_time, worker_ID, turnaround_time):
        """
        The final JSON string will be as follows:
        {
            "worker_id":<worker_id>,
            "job_id":<job_id>,
            "task family": <("map_tasks"|"reduce_tasks")>,
            "task":[
                    {
                    "task_id": "<task_id>",
                    "start time": <arrival_time_of_task_at_Worker>,
                    "end time": <end_time_of_task_in_Worker>,
                    "task turnaround time": <in seconds>
                    },
                    ]
        }
        """
        msg_dict = {}
        msg_dict["worker_id"] = worker_ID
        msg_dict["job_id"] = job_ID
        msg_dict["task family"] = task_family
        msg_dict["task"] = [
                            {
                                "task_id": task_ID,
                                "start time": start_time,
                                "end time": end_time,
                                "task turnaround time": turnaround_time
                            }
                            ]
        return json.dumps(msg_dict)

    @staticmethod
    def prettyPrintMessageToWorker(job_ID, task_family, task_ID, duration,
                                   worker_ID):
        """
        The final JSON string will be as follows:
        {
            "worker_id": <worker_id>,
            "job_id": <job_id>,
            "task family": <("map_tasks"|"reduce_tasks")>,
            "task":[
                    {
                        "task_id": "<task_id>",
                        "duration": <in seconds>
                    },
                    ]
        }
        """
        msg_dict = {}
        msg_dict["worker_id"] = worker_ID
        msg_dict["job_id"] = job_ID
        msg_dict["task family"] = task_family
        msg_dict["task"] = [
                            {
                                "task_id": task_ID,
                                "duration": duration
                            }
                            ]
        print(json.dumps(msg_dict, indent=4))

    @staticmethod
    def prettyPrintMessageToMaster(job_ID, task_family, task_ID, start_time,
                                   end_time, worker_ID, turnaround_time):
        """
        The final JSON string will be as follows:
        {
            "worker_id":<worker_id>,
            "job_id":<job_id>,
            "task family": <("map_tasks"|"reduce_tasks")>,
            "task":[
                    {
                    "task_id": "<task_id>",
                    "start time": <arrival_time_of_task_at_Worker>,
                    "end time": <end_time_of_task_in_Worker>,
                    "task turnaround time": <in seconds>
                    },
                    ]
        }
        """
        msg_dict = {}
        msg_dict["worker_id"] = worker_ID
        msg_dict["job_id"] = job_ID
        msg_dict["task family"] = task_family
        msg_dict["task"] = [
                            {
                                "task_id": task_ID,
                                "start time": start_time,
                                "end time": end_time,
                                "task turnaround time": turnaround_time
                            }
                            ]
        print(json.dumps(msg_dict, indent=4))
