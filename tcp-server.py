#!/usr/bin/python3

import socket

clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#host = '10.16.90.122'
host = socket.gethostname()

port = 444

clientsocket.connect(('10.16.90.122', port))

message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))

