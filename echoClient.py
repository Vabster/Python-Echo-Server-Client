from socket import *
import socket
import sys

### Author: Dillon McCullough###

# Makes sure user submitted input
if len(sys.argv) < 2:
    print "No statement given. Exiting"
    sys.exit(0)

""" Connects to a server, takes user input, sends it to the server, and receives message back """
# Sets the port to 12345
port = 12345
# Sets the hostName to host name IPv4
hostName = gethostname()
userInput = ""

# Creates list to store command line args, exits otherwise
commandArgs = sys.argv[1:]
for a in commandArgs:
    """ Adds single element of commandArgs to user input, also adds a space """
    userInput = userInput + " " + a

# Strips input of any unneeded spaces
userInput = userInput.strip()

# Creates the client socket
clientSocket = socket.socket(AF_INET, SOCK_STREAM)

# Connects the socket to the associated host name and port number
clientSocket.connect((hostName, port))

# Sends user input to server
clientSocket.send(userInput)

#Receives message back from server
serverResponse = clientSocket.recv(1024)
# Prints repsonse from server
print serverResponse

clientSocket.close()
