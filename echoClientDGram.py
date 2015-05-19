from socket import gethostbyname
import socket
import sys

### Author: Dillon McCullough ###

# Makes sure user submitted input, exits otherwise
if len(sys.argv) < 2:
    print "No statement given. Exiting"
    sys.exit(0)

""" Takes user input, sends it to the server, and receives message back """
# Gets the server host
hostName = socket.gethostbyname(socket.gethostname())
# Sets port to 10000
port = 10000

# Creates client socket
clientSocket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

# Initializes user input
userInput = ""

# Creates list to store command line args
commandArgs = sys.argv[1:]
for a in commandArgs:
    """ Adds single element of commandArgs to user input, also adds a space """
    userInput = userInput + " " + a

# Strips input of any unneeded spaces
userInput = userInput.strip()

clientSocket.sendto(userInput,(hostName, port))
# Receives message back from server
serverResponse, server = clientSocket.recvfrom(2048)
# Prints message from server
print serverResponse


