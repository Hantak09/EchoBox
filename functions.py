import socket

def local_ip() -> str:
    return socket.gethostbyname(socket.gethostname())