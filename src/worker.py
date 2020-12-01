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

MESSAGE_BUFFER_SIZE=4096




_TASK_COMPLETION_RESPONSE_ADDR=(socket.gethostname(), 5001) #Master port which takes updates on task completion from the worker
workerToMasterCompletionSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
workerToMasterCompletionSocket.bind(_TASK_COMPLETION_RESPONSE_ADDR)
workerToMasterCompletionSocket.send(task_completition_msg.encode())

if __name__ == "__main__":
    # The CLI to the program will be python worker.py port id
    port_number=int(sys.argv[1])
    worker_id=int(sys.argv[2])

    #Creating the socket tuple for the worker where it will listen to task requests from the master
    _TASK_REQUEST_ADDR=(socket.gethostname(), port_number)
    worker_instance=Worker(worker_id) #Instantiating instance of Worker class

    workerPortConnSocket=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    workerPortConnSocket.bind(_TASK_REQUEST_ADDR) #Binding the socket to the socket tuple created above
    workerPortConnSocket.listen() #Listens for any connections
    masterConn, masterAddr = workerPortConnSocket.accept() #Accepts the connection with return value being (new socket object usable to send and recv data, address bound
                                                       # to the socket on the other end of the connection)
    taskRequest=masterConn.recv(MESSAGE_BUFFER_SIZE) #To extract the message sent
    if not taskRequest:
        masterConn.close()
    threading.Thread(name="Received Task Request From Master", target=Worker.listenForTask(worker_instance,taskRequest),args=masterConn)
