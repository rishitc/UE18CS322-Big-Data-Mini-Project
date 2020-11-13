import socket
from typing import Tuple


class GeneralRequestSocket:
    def __init__(self, ip: str = '', port: int = 5000) -> None:
        """__init__ Store the IP address, port no. of the socket
        and create the socket object

        :param ip: Specifies the IP address of the socket, defaults to ''
        :type ip: str, optional
        :param port: Specifies the port no. of the socket, defaults to 5000
        :type port: int, optional
        """
        self.ip = ip
        self.port = port
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def getAddr(self) -> Tuple:
        """getAddr Return the address tuple (IP Address, Port No.)
        for the socket

        :return: Return the address tuple (IP Address, Port No.)
        for the socket
        :rtype: Tuple
        """
        return (self.ip, self.port)

    def socketSetup(self, noOfBacklogConnections: int = 2):
        """socketSetup Binds the socket to the socket address tuple and
        makes the socket listen on that socket

        :param noOfBacklogConnections: Specifies the number of unaccepted
        connections that the system will allow before refusing new
        connections., defaults to 2
        :type noOfBacklogConnections: int, optional
        """
        self.socket.bind(self.getAddr())
        self.socket.listen(noOfBacklogConnections)
