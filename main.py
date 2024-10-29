import socket
import time
import base64

import threading
from functions import *

PORT = 5000

def main():
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection.bind(("192.168.149.162", PORT))

    def x():
        while True:
            message = connection.recv(1024)
            message = message.decode('utf-8')
            print(f"Received : {message}")

    rxr = threading.Thread(target=x)
    rxr.start()

    while True:
        data = input("Message: ")
        data = data.encode()
        connection.sendto(data, ("192.168.149.71", PORT))


if __name__ == '__main__':
    main()
