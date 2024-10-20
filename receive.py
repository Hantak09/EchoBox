import socket

def receive(connection: socket.socket):
    while True:
        message = connection.recvfrom(1024)
        print(message)