import socket
import sys


TEST_PORT_NO = int(sys.argv[1])

test_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

test_socket.connect((socket.gethostname(), TEST_PORT_NO))
print(f"Connected to socket {TEST_PORT_NO}")