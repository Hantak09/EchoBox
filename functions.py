import socket

def local_ip():
        return socket.gethostbyname(socket.gethostname())