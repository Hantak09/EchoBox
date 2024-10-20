import time

import receive
import threading
from functions import *

PORT = 6969

def main():
    temp = "192.168.1.2"
    connection = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    connection.bind((local_ip(), PORT))

    msg = b"something random here!"
    receive_tread = threading.Thread(target=receive.receive, args=[connection])
    connection.sendto(msg,(temp, PORT))
    time.sleep(1)
    connection.sendto(msg,(temp, PORT))
    connection.sendto(msg,(temp, PORT))
    time.sleep(2)
    connection.sendto(msg,(temp, PORT))



if __name__ == '__main__':
    main()
