#!/usr/bin/python3

# Script Name:      TCP Client
# Author:           Vincent Bailey
# Last Rev:         02/23/2023
# Purpose:          This script will create a TCP client.
# Source:           https://youtu.be/ugYfJNTawks

##############################################################################
# Libraries
##############################################################################
import socket

##############################################################################
# Variables
##############################################################################
clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = socket.gethostname()
port = 444

##############################################################################
# Main Function
##############################################################################
# The server's IP address must be included for the client script to call this script.
# An example of this would be to replace 'host' with the desired host's IP address.
# clientsocket.connect(('192.168.blah.blah', port))
clientsocket.connect((host, port))

# the code line below specifies how much data will be received throught the port.
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))