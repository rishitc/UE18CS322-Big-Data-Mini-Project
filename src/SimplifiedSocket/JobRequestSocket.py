from .GeneralRequestSocket import GeneralRequestSocket
import socket


class JobRequestSocket(GeneralRequestSocket):
    """JobRequestSocket Generating the document

    :param GeneralRequestSocket: [description]
    :type GeneralRequestSocket: [type]
    """
    def __init__(self, ip: str = socket.gethostname(),
                 port: int = 5000) -> None:
        super().__init__(ip, port)
