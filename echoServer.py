#!/usr/bin/env python
import socket
import sys

### Author: Dillon McCullough###

""" TCP Server """
""" Waits for connection from client, then a response from client and echos client response back to the client """
# Initalizes socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# Sets port number to 12345
port = 12345
print ("Server is on")

# Binds socket to port, the '' makes it where the host name
# will be the ipv4 of the local machine
s.bind((socket.gethostname(), port))

# Can have a max of 5 clients
s.listen(5)

# Initializes data to "" which will eventually store data from client
while True:
    """Accepts client, receives a single line from client and sends the line back to client"""
    # waits for a client to accept
    c,addr = s.accept()
    print("accepted")
    # Receives string from client
    data =  c.recv(1024)
    # Once the user presses enter in the client it outputs the information to
    # the server and then to the client
    if data:
        c.send("You Said: " + data)
c.close()



