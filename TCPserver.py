#!/usr/bin/python3

# Script Name:      TCP Server
# Author:           Vincent Bailey
# Last Rev:         02/23/2023
# Purpose:          This script will create a TCP server.
# Source:           https://youtu.be/F1QI9tNuDQg

##############################################################################
# Libraries
##############################################################################
import socket

##############################################################################
# Variables
##############################################################################
# socket.AF_INET tells pythin that we will be creating a socket connection over IPV4.
#
# socket.SOCK_STREAM tells python that we will be establishing a TCP connection.

serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 444

##############################################################################
# Main Function
##############################################################################
# .bind will bind the host and port values in the Variables section together.
#
# .listen will specify how many connections the function will listen to at a time.
# This means that if you are trying to access your server from multiple machines,
# .listen can determine how many machines can be actively connected at once.
# It's currently set to 3 at the moment, which means that our server will actively
# listen to three machines at the same time.

serversocket.bind((host,port))
serversocket.listen(3)

while True:
    clientsocket, address = serversocket.accept()
    print("Received connection from: %s " % str(address))

    message = 'Welcome to the Cerberus Network!' + "\r\n"
    clientsocket.send(message.encode('ascii'))

    clientsocket.close() # this closes the socket connection while any of this information is true.
