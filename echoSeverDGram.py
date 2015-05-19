from socket import *
import sys

### Authors: Dillon McCullough, Eric Smith, Matthew Collins ###

""" UDP Server """
""" Waits for response from client and echos client response back to the client """
# Sets port number to 10000
port = 10000
# Creates the server socket
serverSocket = socket(AF_INET, SOCK_DGRAM)

# Binds host name ('' means machine name) to port
serverSocket.bind(('', port))
# Lets user know server has started
print "Server is on:"

while True:
    """ Receives a one line message from client and then sends that message bac to client """
    # Takes input from client
    message, client = serverSocket.recvfrom(1024)
    # Creates the message to send back to client
    sendBack = "You said: " + message
    # Sends message back to the client
    serverSocket.sendto(sendBack, client)
