import json
import socket
import sys
import threading
from WorkerSim.WorkerSimulation import Worker

"""
Some of the important pointers to be implemented in this code are:-
1) Receiving the worker instance's port number and ID(in string, need to convert to integer) through CLI and binding socket to that address
2) Listening for task launch requests from the Master's port 5001 and then simulating the execution using WorkerSimulation
3) Sharing updates with the master
"""
# The CLI to the program will be python worker.py port id
port_number=int(sys.argv[1])
worker_id=int(sys.argv[2])

_TASK_REQUEST_ADDR=(socket.gethostname(), port_number)
worker_instance=Worker(worker_id)

workerPortConnSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
workerPortConnSocket.bind(_TASK_REQUEST_ADDR)
workerPortConnSocket.listen()
masterConn, masterAddr = workerPortConnSocket.accept()



