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
clientsocket.connect(('192.168.1.120', port))

# the code line below specifies how much data will be received throught the port.
message = clientsocket.recv(1024)

clientsocket.close()

print(message.decode('ascii'))