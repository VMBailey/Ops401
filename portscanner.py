#!/usr/bin/python3

# Script Name:      Port Scanner
# Author:           Vincent Bailey
# Last Rev:         02/27/2023
# Purpose:          This script will determine if a port is open on a designated IP address.
# Source:           https://youtu.be/z_qkqZS7KZ4

##############################################################################
# Libraries
##############################################################################
import socket

##############################################################################
# Variables
##############################################################################
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
host = input("Enter your target address: ")
port = int(input("Alright, now enter the port: "))
s.settimeout(5)

##############################################################################
# Port Scanner Function
##############################################################################
def portscanner(port):
    if s.connect_ex((host, port)):
        print("This port is closed for business.")
    else:
        print("This port is open for business!")
    

##############################################################################
# Main
##############################################################################
portscanner(port)
##############################################################################
# End
##############################################################################