#!/usr/bin/python3

# Script Name:      Port Scanner
# Author:           Vincent Bailey
# Last Rev:         12/7/2021
# Purpose:          This script will scan for open ports on a designtaed IP address.
# Resource:         https://docs.python.org/3/library/socket.html

import socket
import time

sockmod = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
timeout = timeout=5
sockmod.settimeout(timeout)

hostip = input("Please enter a hostIP address: ")
portno = input("Please enter a port number: ")

def portScanner(portno):
    if sockmod.socket((hostip, portno)):
        print("Port closed")
    else:
        print("Port open")

portScanner(portno)