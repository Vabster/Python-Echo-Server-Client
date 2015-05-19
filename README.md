# Python-Echo-Server-Client
Simple Python Implementation of a Echo Server/Client

echoServer.py and echoClient.py is a TCP implementation of the Echo Server/Client

echoServerDGram.py and echoClientDGram.py is a UDP implementation of the Echo Server/Client

In order to run the TCP version. first run python echoServer.py and then run python echoClient.py "{Echo Response]"

Example:
python echoServer.py
python echoClient.py "Hello Friend"

Running these two commands, the client output would be "You said: Hello Friend"

In order to run the UDP version. first run python echoServerDGram.py and then run python echoClientDGram.py "{Echo Response]"

Example:
python echoServerDGram.py
python echoClientDGram.py "Hello Friend"

Running these two commands, the client output would be "You said: Hello Friend"
