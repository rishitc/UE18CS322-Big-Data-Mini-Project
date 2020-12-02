import socket
import sys
import threading
from WorkerSim.WorkerSimulation import Worker

"""
Some of the important pointers to be implemented in this code are:
1) Receiving the worker instance's port number and ID(in string, need to
   convert to integer) through CLI and binding socket to that address.
2) Listening for task launch requests from the Master's port 5001 and then
   simulating the execution using WorkerSimulation.
3) Sharing updates with the master.
"""

MESSAGE_BUFFER_SIZE = 4096


def getCMDLineArgs():
    """```getCMDLineArgs``` returns the command line arguments
    in order of ```port number``` and ```worker ID```

    ```return```: Tuple containing ```port number``` and ```worker ID```

    ```rtype```: Tuple[int, int]
    """
    return int(sys.argv[1]), int(sys.argv[2])


def createWorkerSocket(task_request_addr):
    """ ```createWorkerSocket``` returns a socket that will be used
    to connect worker to its designated port in order to listen for
    task requests from the master.

    ```return```: Socket object

    ```rtype```: socket.socket
    """
    socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_object.bind(task_request_addr)
    return socket_object


def createMasterSocket(task_complete_addr):
    """ ```createSocket``` returns a socket that will be used
    to connect to the master.

    ```return```: Socket object

    ```rtype```: socket.socket
    """
    socket_object = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket_object.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    socket_object.connect(task_complete_addr)
    return socket_object


if __name__ == "__main__":
    # The CLI to the program will be python worker.py port id
    port_number, worker_id = getCMDLineArgs()

    # Creating the socket tuple for the worker where
    # it will listen to task requests from the master
    _TASK_REQUEST_ADDR = (socket.gethostname(), port_number)
    worker_instance = Worker(worker_id)  # Instance of Worker class
    workerPortConnSocket = createWorkerSocket(_TASK_REQUEST_ADDR)
    workerPortConnSocket.listen()
    # workerPortConnSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # workerPortConnSocket.bind(_TASK_REQUEST_ADDR) # Binding the socket
    # to the socket tuple created above
    # workerPortConnSocket.listen()  # Listens for any connections
    masterConn, masterAddr = workerPortConnSocket.accept()  # Accepts the
    # connection with return value being (new socket object usable to send and
    # recv data, address bound to the socket on the other end of the connection
    # ---

    input("Have all the workers connected??")

    _TASK_COMPLETION_RESPONSE_ADDR = (socket.gethostname(), 5001)  # Master
    # port which takes updates on task completion from the worker
    workerToMasterCompletionSocket = \
        createMasterSocket(_TASK_COMPLETION_RESPONSE_ADDR)
    workerToMasterCompletionSocket.sendall(str(worker_id).encode())
    # Creating all the threads
    json_receive_master = threading.Thread(name="Sending Task To Exec Pool",
                                           target=worker_instance.
                                           listenForTaskRequest,
                                           args=(masterConn,))
    json_receive_master.daemon = True
    json_receive_master.start()

    json_simulate_task = threading\
        .Thread(name="Worker Instance Simulation",
                target=worker_instance.simulateWorker)
    json_simulate_task.daemon = True
    json_simulate_task.start()

    json_reply_master = threading\
        .Thread(name=("Sending Task Completion "
                      "From Worker To Master"),
                target=worker_instance.taskComplete,
                args=(workerToMasterCompletionSocket,))
    json_reply_master.daemon = True
    json_reply_master.start()

    # Joining the threads
    json_receive_master.join()
    json_simulate_task.join()
    json_reply_master.join()

    # Closing the sockets
    workerPortConnSocket.close()
    workerToMasterCompletionSocket.close()
