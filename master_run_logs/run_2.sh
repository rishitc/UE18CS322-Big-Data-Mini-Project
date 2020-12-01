Number of map tasks: 
Number of reduce tasks:
Total Number of tasks

-----
client.py
-----

 Job request : {'job_id': '0', 'map_tasks': [{'task_id': '0_M0', 'duration': 2}, {'task_id': '0_M1', 'duration': 1}], 'reduce_tasks': [{'task_id': '0_R0', 'duration': 3}, {'task_id': '0_R1', 'duration': 3}]}
interval:  0.5296500575858202 
 Job request : {'job_id': '1', 'map_tasks': [{'task_id': '1_M0', 'duration': 1}, {'task_id': '1_M1', 'duration': 1}, {'task_id': '1_M2', 'duration': 2}], 'reduce_tasks': [{'task_id': '1_R0', 'duration': 3}, {'task_id': '1_R1', 'duration': 4}]}
interval:  2.6848986076535035 
 Job request : {'job_id': '2', 'map_tasks': [{'task_id': '2_M0', 'duration': 1}, {'task_id': '2_M1', 'duration': 2}, {'task_id': '2_M2', 'duration': 2}], 'reduce_tasks': [{'task_id': '2_R0', 'duration': 3}, {'task_id': '2_R1', 'duration': 4}]}
interval:  0.09867203545844898 
 Job request : {'job_id': '3', 'map_tasks': [{'task_id': '3_M0', 'duration': 4}, {'task_id': '3_M1', 'duration': 2}], 'reduce_tasks': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}
interval:  1.318763156316299 
 Job request : {'job_id': '4', 'map_tasks': [{'task_id': '4_M0', 'duration': 2}, {'task_id': '4_M1', 'duration': 2}, {'task_id': '4_M2', 'duration': 4}], 'reduce_tasks': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}
interval:  2.040106641617886 
 Job request : {'job_id': '5', 'map_tasks': [{'task_id': '5_M0', 'duration': 4}, {'task_id': '5_M1', 'duration': 2}, {'task_id': '5_M2', 'duration': 3}], 'reduce_tasks': [{'task_id': '5_R0', 'duration': 4}]}
interval:  0.8411559850923908 
 Job request : {'job_id': '6', 'map_tasks': [{'task_id': '6_M0', 'duration': 4}, {'task_id': '6_M1', 'duration': 2}], 'reduce_tasks': [{'task_id': '6_R0', 'duration': 4}]}
interval:  0.38949884930873674 
 Job request : {'job_id': '7', 'map_tasks': [{'task_id': '7_M0', 'duration': 3}, {'task_id': '7_M1', 'duration': 2}], 'reduce_tasks': [{'task_id': '7_R0', 'duration': 4}]}
interval:  1.1286000304231287 
 Job request : {'job_id': '8', 'map_tasks': [{'task_id': '8_M0', 'duration': 3}, {'task_id': '8_M1', 'duration': 2}, {'task_id': '8_M2', 'duration': 4}], 'reduce_tasks': [{'task_id': '8_R0', 'duration': 3}]}
interval:  1.5292024483821094 
 Job request : {'job_id': '9', 'map_tasks': [{'task_id': '9_M0', 'duration': 2}, {'task_id': '9_M1', 'duration': 4}, {'task_id': '9_M2', 'duration': 3}, {'task_id': '9_M3', 'duration': 1}], 'reduce_tasks': [{'task_id': '9_R0', 'duration': 3}]}


------
Have the 3 workers been started, yet? [y/n] y
worker["port"]=4000
worker["port"]=4001
worker["port"]=4002
JobUpdateTracker Initialized
Job Tracker Initialized
Inside listenForJobRequests
INFO: Listening to updates from the workers on port: 5001
INFO: Connected to worker ID: 1 at address:
IP Address: 127.0.0.1
Socket: 39514
INFO: Connected to worker ID: 2 at address:
IP Address: 127.0.0.1
Socket: 39516
INFO: Connected to worker ID: 3 at address:
IP Address: 127.0.0.1
Socket: 39518
workerUpdateThreads=[<Thread(Worker-1 Update Listener, started daemon 140225566693120)>, <Thread(Worker-2 Update Listener, started daemon 140225558300416)>, <Thread(Worker-3 Update Listener, started daemon 140225549907712)>]
You have reached the bottom of the '__main__'
[<_MainThread(MainThread, started 140225593648960)>, <Thread(Listen for Incoming JobRequests, started daemon 140225583478528)>, <Thread(Job Dispatcher -Round-Robin Scheduling, started daemon 140225575085824)>, <Thread(Worker-1 Update Listener, started daemon 140225566693120)>, <Thread(Worker-2 Update Listener, started daemon 140225558300416)>, <Thread(Worker-3 Update Listener, started daemon 140225549907712)>]
Something connected to me!! ('127.0.0.1', 39908)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39908
jobRequestHandler.jobRequests={'0': {'map': [{'task_id': '0_M0', 'duration': 2}, {'task_id': '0_M1', 'duration': 1}], 'reduce': [{'task_id': '0_R0', 'duration': 3}, {'task_id': '0_R1', 'duration': 3}]}}
Selected tuple: ('0', 'map', {'task_id': '0_M0', 'duration': 2})
Sending task to worker: {"worker_id": 1, "job_id": "0", "task family": "map", "task": {"task_id": "0_M0", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 4, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 7, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 3, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'0': {'map': [{'task_id': '0_M1', 'duration': 1}], 'reduce': [{'task_id': '0_R0', 'duration': 3}, {'task_id': '0_R1', 'duration': 3}]}}
Selected tuple: ('0', 'map', {'task_id': '0_M1', 'duration': 1})
Sending task to worker: {"worker_id": 2, "job_id": "0", "task family": "map", "task": {"task_id": "0_M1", "duration": 1}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 4, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 3, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'0': {'map': [], 'reduce': [{'task_id': '0_R0', 'duration': 3}, {'task_id': '0_R1', 'duration': 3}]}}
Received worker update at master: {"worker_id": 2, "job_id": "0", "task family": "map", "task": {"task_id": "0_M1", "start time": 1606858926.1470585, "end time": 1606858926.1777234}}
Something connected to me!! ('127.0.0.1', 39910)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39910
jobRequestHandler.jobRequests={'0': {'map': [], 'reduce': [{'task_id': '0_R0', 'duration': 3}, {'task_id': '0_R1', 'duration': 3}]}, '1': {'map': [{'task_id': '1_M0', 'duration': 1}, {'task_id': '1_M1', 'duration': 1}, {'task_id': '1_M2', 'duration': 2}], 'reduce': [{'task_id': '1_R0', 'duration': 3}, {'task_id': '1_R1', 'duration': 4}]}}
Selected tuple: ('1', 'map', {'task_id': '1_M0', 'duration': 1})
Sending task to worker: {"worker_id": 3, "job_id": "1", "task family": "map", "task": {"task_id": "1_M0", "duration": 1}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 4, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 7, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'0': {'map': [], 'reduce': [{'task_id': '0_R0', 'duration': 3}, {'task_id': '0_R1', 'duration': 3}]}, '1': {'map': [{'task_id': '1_M1', 'duration': 1}, {'task_id': '1_M2', 'duration': 2}], 'reduce': [{'task_id': '1_R0', 'duration': 3}, {'task_id': '1_R1', 'duration': 4}]}}
Selected tuple: ('1', 'map', {'task_id': '1_M1', 'duration': 1})
Sending task to worker: {"worker_id": 1, "job_id": "1", "task family": "map", "task": {"task_id": "1_M1", "duration": 1}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 3, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 7, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'0': {'map': [], 'reduce': [{'task_id': '0_R0', 'duration': 3}, {'task_id': '0_R1', 'duration': 3}]}, '1': {'map': [{'task_id': '1_M2', 'duration': 2}], 'reduce': [{'task_id': '1_R0', 'duration': 3}, {'task_id': '1_R1', 'duration': 4}]}}
Selected tuple: ('1', 'map', {'task_id': '1_M2', 'duration': 2})
Sending task to worker: {"worker_id": 2, "job_id": "1", "task family": "map", "task": {"task_id": "1_M2", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 3, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'0': {'map': [], 'reduce': [{'task_id': '0_R0', 'duration': 3}, {'task_id': '0_R1', 'duration': 3}]}, '1': {'map': [], 'reduce': [{'task_id': '1_R0', 'duration': 3}, {'task_id': '1_R1', 'duration': 4}]}}
Received worker update at master: {"worker_id": 3, "job_id": "1", "task family": "map", "task": {"task_id": "1_M0", "start time": 1606858926.3465524, "end time": 1606858926.3773355}}
Received worker update at master: {"worker_id": 1, "job_id": "0", "task family": "map", "task": {"task_id": "0_M0", "start time": 1606858926.0554733, "end time": 1606858927.091953}}
Received worker update at master: {"worker_id": 1, "job_id": "1", "task family": "map", "task": {"task_id": "1_M1", "start time": 1606858926.346918, "end time": 1606858927.0921714}}
Selected tuple: ('0', 'reduce', {'task_id': '0_R0', 'duration': 3})
Sending task to worker: {"worker_id": 3, "job_id": "0", "task family": "reduce", "task": {"task_id": "0_R0", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 5, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'0': {'map': [], 'reduce': [{'task_id': '0_R1', 'duration': 3}]}, '1': {'map': [], 'reduce': [{'task_id': '1_R0', 'duration': 3}, {'task_id': '1_R1', 'duration': 4}]}}
Selected tuple: ('0', 'reduce', {'task_id': '0_R1', 'duration': 3})
Sending task to worker: {"worker_id": 1, "job_id": "0", "task family": "reduce", "task": {"task_id": "0_R1", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 4, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'1': {'map': [], 'reduce': [{'task_id': '1_R0', 'duration': 3}, {'task_id': '1_R1', 'duration': 4}]}}
Received worker update at master: {"worker_id": 2, "job_id": "1", "task family": "map", "task": {"task_id": "1_M2", "start time": 1606858926.3572621, "end time": 1606858928.206108}}
Selected tuple: ('1', 'reduce', {'task_id': '1_R0', 'duration': 3})
Sending task to worker: {"worker_id": 2, "job_id": "1", "task family": "reduce", "task": {"task_id": "1_R0", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 4, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'1': {'map': [], 'reduce': [{'task_id': '1_R1', 'duration': 4}]}}
Selected tuple: ('1', 'reduce', {'task_id': '1_R1', 'duration': 4})
Sending task to worker: {"worker_id": 3, "job_id": "1", "task family": "reduce", "task": {"task_id": "1_R1", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 4, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={}
Something connected to me!! ('127.0.0.1', 39912)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39912
jobRequestHandler.jobRequests={'2': {'map': [{'task_id': '2_M0', 'duration': 1}, {'task_id': '2_M1', 'duration': 2}, {'task_id': '2_M2', 'duration': 2}], 'reduce': [{'task_id': '2_R0', 'duration': 3}, {'task_id': '2_R1', 'duration': 4}]}}
Selected tuple: ('2', 'map', {'task_id': '2_M0', 'duration': 1})
Sending task to worker: {"worker_id": 1, "job_id": "2", "task family": "map", "task": {"task_id": "2_M0", "duration": 1}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 3, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'2': {'map': [{'task_id': '2_M1', 'duration': 2}, {'task_id': '2_M2', 'duration': 2}], 'reduce': [{'task_id': '2_R0', 'duration': 3}, {'task_id': '2_R1', 'duration': 4}]}}
Selected tuple: ('2', 'map', {'task_id': '2_M1', 'duration': 2})
Sending task to worker: {"worker_id": 2, "job_id": "2", "task family": "map", "task": {"task_id": "2_M1", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 3, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'2': {'map': [{'task_id': '2_M2', 'duration': 2}], 'reduce': [{'task_id': '2_R0', 'duration': 3}, {'task_id': '2_R1', 'duration': 4}]}}
Selected tuple: ('2', 'map', {'task_id': '2_M2', 'duration': 2})
Sending task to worker: {"worker_id": 3, "job_id": "2", "task family": "map", "task": {"task_id": "2_M2", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 3, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'2': {'map': [], 'reduce': [{'task_id': '2_R0', 'duration': 3}, {'task_id': '2_R1', 'duration': 4}]}}
Something connected to me!! ('127.0.0.1', 39914)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39914
jobRequestHandler.jobRequests={'2': {'map': [], 'reduce': [{'task_id': '2_R0', 'duration': 3}, {'task_id': '2_R1', 'duration': 4}]}, '3': {'map': [{'task_id': '3_M0', 'duration': 4}, {'task_id': '3_M1', 'duration': 2}], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}}
Selected tuple: ('3', 'map', {'task_id': '3_M0', 'duration': 4})
Sending task to worker: {"worker_id": 1, "job_id": "3", "task family": "map", "task": {"task_id": "3_M0", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'2': {'map': [], 'reduce': [{'task_id': '2_R0', 'duration': 3}, {'task_id': '2_R1', 'duration': 4}]}, '3': {'map': [{'task_id': '3_M1', 'duration': 2}], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}}
Selected tuple: ('3', 'map', {'task_id': '3_M1', 'duration': 2})
Sending task to worker: {"worker_id": 2, "job_id": "3", "task family": "map", "task": {"task_id": "3_M1", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 4, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'2': {'map': [], 'reduce': [{'task_id': '2_R0', 'duration': 3}, {'task_id': '2_R1', 'duration': 4}]}, '3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}}
Received worker update at master: {"worker_id": 1, "job_id": "2", "task family": "map", "task": {"task_id": "2_M0", "start time": 1606858929.0364468, "end time": 1606858929.1401465}}
Received worker update at master: {"worker_id": 3, "job_id": "0", "task family": "reduce", "task": {"task_id": "0_R0", "start time": 1606858927.1080844, "end time": 1606858929.4323041}}
Received worker update at master: {"worker_id": 1, "job_id": "0", "task family": "reduce", "task": {"task_id": "0_R1", "start time": 1606858927.1234553, "end time": 1606858930.1464548}}
Received worker update at master: {"worker_id": 2, "job_id": "2", "task family": "map", "task": {"task_id": "2_M1", "start time": 1606858929.0416853, "end time": 1606858930.268219}}
Received worker update at master: {"worker_id": 2, "job_id": "3", "task family": "map", "task": {"task_id": "3_M1", "start time": 1606858929.1477084, "end time": 1606858930.2683475}}
Something connected to me!! ('127.0.0.1', 39916)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39916
Received worker update at master: {"worker_id": 3, "job_id": "2", "task family": "map", "task": {"task_id": "2_M2", "start time": 1606858929.0570393, "end time": 1606858930.4437559}}
Selected tuple: ('2', 'reduce', {'task_id': '2_R0', 'duration': 3})
jobRequestHandler.jobRequests={'2': {'map': [], 'reduce': [{'task_id': '2_R1', 'duration': 4}]}, '3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [{'task_id': '4_M0', 'duration': 2}, {'task_id': '4_M1', 'duration': 2}, {'task_id': '4_M2', 'duration': 4}], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}}
Sending task to worker: {"worker_id": 3, "job_id": "2", "task family": "reduce", "task": {"task_id": "2_R0", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 4, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'2': {'map': [], 'reduce': [{'task_id': '2_R1', 'duration': 4}]}, '3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [{'task_id': '4_M0', 'duration': 2}, {'task_id': '4_M1', 'duration': 2}, {'task_id': '4_M2', 'duration': 4}], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}}
Selected tuple: ('2', 'reduce', {'task_id': '2_R1', 'duration': 4})
Sending task to worker: {"worker_id": 1, "job_id": "2", "task family": "reduce", "task": {"task_id": "2_R1", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 3, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [{'task_id': '4_M0', 'duration': 2}, {'task_id': '4_M1', 'duration': 2}, {'task_id': '4_M2', 'duration': 4}], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}}
Selected tuple: ('4', 'map', {'task_id': '4_M0', 'duration': 2})
Sending task to worker: {"worker_id": 2, "job_id": "4", "task family": "map", "task": {"task_id": "4_M0", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 3, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [{'task_id': '4_M1', 'duration': 2}, {'task_id': '4_M2', 'duration': 4}], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}}
Selected tuple: ('4', 'map', {'task_id': '4_M1', 'duration': 2})
Sending task to worker: {"worker_id": 3, "job_id": "4", "task family": "map", "task": {"task_id": "4_M1", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 3, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [{'task_id': '4_M2', 'duration': 4}], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}}
Selected tuple: ('4', 'map', {'task_id': '4_M2', 'duration': 4})
Sending task to worker: {"worker_id": 1, "job_id": "4", "task family": "map", "task": {"task_id": "4_M2", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}}
Received worker update at master: {"worker_id": 2, "job_id": "1", "task family": "reduce", "task": {"task_id": "1_R0", "start time": 1606858928.2116072, "end time": 1606858931.2745237}}
Received worker update at master: {"worker_id": 3, "job_id": "1", "task family": "reduce", "task": {"task_id": "1_R1", "start time": 1606858928.23206, "end time": 1606858931.460105}}
Received worker update at master: {"worker_id": 2, "job_id": "4", "task family": "map", "task": {"task_id": "4_M0", "start time": 1606858930.4873044, "end time": 1606858932.2799394}}
Received worker update at master: {"worker_id": 3, "job_id": "4", "task family": "map", "task": {"task_id": "4_M1", "start time": 1606858930.4975412, "end time": 1606858932.4661045}}
Something connected to me!! ('127.0.0.1', 39918)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39918
jobRequestHandler.jobRequests={'3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [{'task_id': '5_M0', 'duration': 4}, {'task_id': '5_M1', 'duration': 2}, {'task_id': '5_M2', 'duration': 3}], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}}
Selected tuple: ('5', 'map', {'task_id': '5_M0', 'duration': 4})
Sending task to worker: {"worker_id": 2, "job_id": "5", "task family": "map", "task": {"task_id": "5_M0", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [{'task_id': '5_M1', 'duration': 2}, {'task_id': '5_M2', 'duration': 3}], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}}
Selected tuple: ('5', 'map', {'task_id': '5_M1', 'duration': 2})
Sending task to worker: {"worker_id": 3, "job_id": "5", "task family": "map", "task": {"task_id": "5_M1", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [{'task_id': '5_M2', 'duration': 3}], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}}
Selected tuple: ('5', 'map', {'task_id': '5_M2', 'duration': 3})
Sending task to worker: {"worker_id": 1, "job_id": "5", "task family": "map", "task": {"task_id": "5_M2", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'3': {'map': [], 'reduce': [{'task_id': '3_R0', 'duration': 1}, {'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}}
Received worker update at master: {"worker_id": 1, "job_id": "3", "task family": "map", "task": {"task_id": "3_M0", "start time": 1606858929.1402469, "end time": 1606858933.2352214}}
Selected tuple: ('3', 'reduce', {'task_id': '3_R0', 'duration': 1})
Sending task to worker: {"worker_id": 2, "job_id": "3", "task family": "reduce", "task": {"task_id": "3_R0", "duration": 1}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'3': {'map': [], 'reduce': [{'task_id': '3_R1', 'duration': 1}]}, '4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}}
Selected tuple: ('3', 'reduce', {'task_id': '3_R1', 'duration': 1})
Sending task to worker: {"worker_id": 3, "job_id": "3", "task family": "reduce", "task": {"task_id": "3_R1", "duration": 1}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}}
Received worker update at master: {"worker_id": 2, "job_id": "3", "task family": "reduce", "task": {"task_id": "3_R0", "start time": 1606858933.250967, "end time": 1606858933.3065453}}
Something connected to me!! ('127.0.0.1', 39920)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39920
jobRequestHandler.jobRequests={'4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [{'task_id': '6_M0', 'duration': 4}, {'task_id': '6_M1', 'duration': 2}], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}}
Selected tuple: ('6', 'map', {'task_id': '6_M0', 'duration': 4})
Sending task to worker: {"worker_id": 1, "job_id": "6", "task family": "map", "task": {"task_id": "6_M0", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [{'task_id': '6_M1', 'duration': 2}], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}}
Selected tuple: ('6', 'map', {'task_id': '6_M1', 'duration': 2})
Sending task to worker: {"worker_id": 2, "job_id": "6", "task family": "map", "task": {"task_id": "6_M1", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}}
Received worker update at master: {"worker_id": 3, "job_id": "2", "task family": "reduce", "task": {"task_id": "2_R0", "start time": 1606858930.4716878, "end time": 1606858933.4723213}}
Received worker update at master: {"worker_id": 3, "job_id": "3", "task family": "reduce", "task": {"task_id": "3_R1", "start time": 1606858933.26126, "end time": 1606858933.4724183}}
Something connected to me!! ('127.0.0.1', 39922)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39922
jobRequestHandler.jobRequests={'4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [{'task_id': '7_M0', 'duration': 3}, {'task_id': '7_M1', 'duration': 2}], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}}
Selected tuple: ('7', 'map', {'task_id': '7_M0', 'duration': 3})
Sending task to worker: {"worker_id": 3, "job_id": "7", "task family": "map", "task": {"task_id": "7_M0", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [{'task_id': '7_M1', 'duration': 2}], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}}
Selected tuple: ('7', 'map', {'task_id': '7_M1', 'duration': 2})
Sending task to worker: {"worker_id": 1, "job_id": "7", "task family": "map", "task": {"task_id": "7_M1", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 0, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'4': {'map': [], 'reduce': [{'task_id': '4_R0', 'duration': 3}, {'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}}
Received worker update at master: {"worker_id": 1, "job_id": "2", "task family": "reduce", "task": {"task_id": "2_R1", "start time": 1606858930.4770103, "end time": 1606858934.2516909}}
Received worker update at master: {"worker_id": 1, "job_id": "4", "task family": "map", "task": {"task_id": "4_M2", "start time": 1606858930.5129435, "end time": 1606858934.251844}}
Selected tuple: ('4', 'reduce', {'task_id': '4_R0', 'duration': 3})
Sending task to worker: {"worker_id": 2, "job_id": "4", "task family": "reduce", "task": {"task_id": "4_R0", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 4, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'4': {'map': [], 'reduce': [{'task_id': '4_R1', 'duration': 3}]}, '5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}}
Selected tuple: ('4', 'reduce', {'task_id': '4_R1', 'duration': 3})
Sending task to worker: {"worker_id": 3, "job_id": "4", "task family": "reduce", "task": {"task_id": "4_R1", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 4, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}}
Received worker update at master: {"worker_id": 3, "job_id": "5", "task family": "map", "task": {"task_id": "5_M1", "start time": 1606858932.5241394, "end time": 1606858934.4785929}}
Something connected to me!! ('127.0.0.1', 39924)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39924
jobRequestHandler.jobRequests={'5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [{'task_id': '8_M0', 'duration': 3}, {'task_id': '8_M1', 'duration': 2}, {'task_id': '8_M2', 'duration': 4}], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}}
Selected tuple: ('8', 'map', {'task_id': '8_M0', 'duration': 3})
Sending task to worker: {"worker_id": 1, "job_id": "8", "task family": "map", "task": {"task_id": "8_M0", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 4, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [{'task_id': '8_M1', 'duration': 2}, {'task_id': '8_M2', 'duration': 4}], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}}
Selected tuple: ('8', 'map', {'task_id': '8_M1', 'duration': 2})
Sending task to worker: {"worker_id": 2, "job_id": "8", "task family": "map", "task": {"task_id": "8_M1", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 3, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [{'task_id': '8_M2', 'duration': 4}], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}}
Selected tuple: ('8', 'map', {'task_id': '8_M2', 'duration': 4})
Sending task to worker: {"worker_id": 3, "job_id": "8", "task family": "map", "task": {"task_id": "8_M2", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 3, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'5': {'map': [], 'reduce': [{'task_id': '5_R0', 'duration': 4}]}, '6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}}
Received worker update at master: {"worker_id": 1, "job_id": "5", "task family": "map", "task": {"task_id": "5_M2", "start time": 1606858932.5344634, "end time": 1606858935.25811}}
Received worker update at master: {"worker_id": 1, "job_id": "7", "task family": "map", "task": {"task_id": "7_M1", "start time": 1606858933.7623208, "end time": 1606858935.2582781}}
Received worker update at master: {"worker_id": 2, "job_id": "6", "task family": "map", "task": {"task_id": "6_M1", "start time": 1606858933.3690293, "end time": 1606858935.3711312}}
Received worker update at master: {"worker_id": 2, "job_id": "5", "task family": "map", "task": {"task_id": "5_M0", "start time": 1606858932.5086083, "end time": 1606858936.3774734}}
Something connected to me!! ('127.0.0.1', 39926)
INFO: Connected to client at address:
IP Address: 127.0.0.1
Socket: 39926
Selected tuple: ('5', 'reduce', {'task_id': '5_R0', 'duration': 4})
jobRequestHandler.jobRequests={'6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}, '9': {'map': [{'task_id': '9_M0', 'duration': 2}, {'task_id': '9_M1', 'duration': 4}, {'task_id': '9_M2', 'duration': 3}, {'task_id': '9_M3', 'duration': 1}], 'reduce': [{'task_id': '9_R0', 'duration': 3}]}}
Sending task to worker: {"worker_id": 1, "job_id": "5", "task family": "reduce", "task": {"task_id": "5_R0", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}, '9': {'map': [{'task_id': '9_M0', 'duration': 2}, {'task_id': '9_M1', 'duration': 4}, {'task_id': '9_M2', 'duration': 3}, {'task_id': '9_M3', 'duration': 1}], 'reduce': [{'task_id': '9_R0', 'duration': 3}]}}
Received worker update at master: {"worker_id": 2, "job_id": "4", "task family": "reduce", "task": {"task_id": "4_R0", "start time": 1606858934.2727914, "end time": 1606858936.3778026}}
Selected tuple: ('9', 'map', {'task_id': '9_M0', 'duration': 2})
Sending task to worker: {"worker_id": 2, "job_id": "9", "task family": "map", "task": {"task_id": "9_M0", "duration": 2}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}, '9': {'map': [{'task_id': '9_M1', 'duration': 4}, {'task_id': '9_M2', 'duration': 3}, {'task_id': '9_M3', 'duration': 1}], 'reduce': [{'task_id': '9_R0', 'duration': 3}]}}
Received worker update at master: {"worker_id": 2, "job_id": "8", "task family": "map", "task": {"task_id": "8_M1", "start time": 1606858934.867663, "end time": 1606858936.3778868}}
Selected tuple: ('9', 'map', {'task_id': '9_M1', 'duration': 4})
Sending task to worker: {"worker_id": 1, "job_id": "9", "task family": "map", "task": {"task_id": "9_M1", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 6, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}, '9': {'map': [{'task_id': '9_M2', 'duration': 3}, {'task_id': '9_M3', 'duration': 1}], 'reduce': [{'task_id': '9_R0', 'duration': 3}]}}
Selected tuple: ('9', 'map', {'task_id': '9_M2', 'duration': 3})
Sending task to worker: {"worker_id": 2, "job_id": "9", "task family": "map", "task": {"task_id": "9_M2", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}, '9': {'map': [{'task_id': '9_M3', 'duration': 1}], 'reduce': [{'task_id': '9_R0', 'duration': 3}]}}
Selected tuple: ('9', 'map', {'task_id': '9_M3', 'duration': 1})
Sending task to worker: {"worker_id": 1, "job_id": "9", "task family": "map", "task": {"task_id": "9_M3", "duration": 1}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 0, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 0, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '7': {'map': [], 'reduce': [{'task_id': '7_R0', 'duration': 4}]}, '8': {'map': [], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}, '9': {'map': [], 'reduce': [{'task_id': '9_R0', 'duration': 3}]}}
Received worker update at master: {"worker_id": 3, "job_id": "7", "task family": "map", "task": {"task_id": "7_M0", "start time": 1606858933.7468693, "end time": 1606858936.5013065}}
Received worker update at master: {"worker_id": 3, "job_id": "4", "task family": "reduce", "task": {"task_id": "4_R1", "start time": 1606858934.2831075, "end time": 1606858936.5014715}}
Selected tuple: ('7', 'reduce', {'task_id': '7_R0', 'duration': 4})
Sending task to worker: {"worker_id": 2, "job_id": "7", "task family": "reduce", "task": {"task_id": "7_R0", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 0, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 4, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'6': {'map': [], 'reduce': [{'task_id': '6_R0', 'duration': 4}]}, '8': {'map': [], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}, '9': {'map': [], 'reduce': [{'task_id': '9_R0', 'duration': 3}]}}
Received worker update at master: {"worker_id": 1, "job_id": "6", "task family": "map", "task": {"task_id": "6_M0", "start time": 1606858933.3535783, "end time": 1606858937.2802436}}
Selected tuple: ('6', 'reduce', {'task_id': '6_R0', 'duration': 4})
Received worker update at master: {"worker_id": 1, "job_id": "8", "task family": "map", "task": {"task_id": "8_M0", "start time": 1606858934.8572266, "end time": 1606858937.2803767}}
Sending task to worker: {"worker_id": 3, "job_id": "6", "task family": "reduce", "task": {"task_id": "6_R0", "duration": 4}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 1, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 4, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 1, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'8': {'map': [], 'reduce': [{'task_id': '8_R0', 'duration': 3}]}, '9': {'map': [], 'reduce': [{'task_id': '9_R0', 'duration': 3}]}}
Received worker update at master: {"worker_id": 1, "job_id": "9", "task family": "map", "task": {"task_id": "9_M3", "start time": 1606858936.433398, "end time": 1606858937.2804997}}
Received worker update at master: {"worker_id": 2, "job_id": "9", "task family": "map", "task": {"task_id": "9_M0", "start time": 1606858936.3922048, "end time": 1606858938.430676}}
Received worker update at master: {"worker_id": 3, "job_id": "8", "task family": "map", "task": {"task_id": "8_M2", "start time": 1606858934.8780518, "end time": 1606858938.5443535}}
Selected tuple: ('8', 'reduce', {'task_id': '8_R0', 'duration': 3})
Sending task to worker: {"worker_id": 1, "job_id": "8", "task family": "reduce", "task": {"task_id": "8_R0", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 2, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={'9': {'map': [], 'reduce': [{'task_id': '9_R0', 'duration': 3}]}}
Received worker update at master: {"worker_id": 2, "job_id": "9", "task family": "map", "task": {"task_id": "9_M2", "start time": 1606858936.4179108, "end time": 1606858939.4370072}}
Received worker update at master: {"worker_id": 1, "job_id": "5", "task family": "reduce", "task": {"task_id": "5_R0", "start time": 1606858936.391983, "end time": 1606858940.359352}}
Received worker update at master: {"worker_id": 1, "job_id": "9", "task family": "map", "task": {"task_id": "9_M1", "start time": 1606858936.412748, "end time": 1606858940.3594937}}
Selected tuple: ('9', 'reduce', {'task_id': '9_R0', 'duration': 3})
Sending task to worker: {"worker_id": 2, "job_id": "9", "task family": "reduce", "task": {"task_id": "9_R0", "duration": 3}}
self.workerState={1: {'slots': 5, 'port': 4000, 'free slots': 4, 'socket': <socket.socket fd=3, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 42402), raddr=('127.0.1.1', 4000)>}, 2: {'slots': 7, 'port': 4001, 'free slots': 5, 'socket': <socket.socket fd=4, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 55660), raddr=('127.0.1.1', 4001)>}, 3: {'slots': 3, 'port': 4002, 'free slots': 2, 'socket': <socket.socket fd=5, family=AddressFamily.AF_INET, type=SocketKind.SOCK_STREAM, proto=0, laddr=('127.0.0.1', 34606), raddr=('127.0.1.1', 4002)>}}
requestHandler.jobRequests={}
Received worker update at master: {"worker_id": 2, "job_id": "7", "task family": "reduce", "task": {"task_id": "7_R0", "start time": 1606858936.5170746, "end time": 1606858940.4534338}}
Received worker update at master: {"worker_id": 3, "job_id": "6", "task family": "reduce", "task": {"task_id": "6_R0", "start time": 1606858937.3010247, "end time": 1606858940.5618758}}
Received worker update at master: {"worker_id": 1, "job_id": "8", "task family": "reduce", "task": {"task_id": "8_R0", "start time": 1606858938.5600939, "end time": 1606858941.3657126}}
Received worker update at master: {"worker_id": 2, "job_id": "9", "task family": "reduce", "task": {"task_id": "9_R0", "start time": 1606858940.385457, "end time": 1606858942.4760592}}
