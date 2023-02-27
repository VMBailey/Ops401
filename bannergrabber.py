#!/usr/bin/python3

# Script Name:      Banner Grabber
# Author:           Vincent Bailey
# Last Rev:         02/27/2023
# Purpose:          This script will display the network banner for a designated target.
# Source:           https://youtu.be/CeGW761BIsA

##############################################################################
# Libraries
##############################################################################
import sys, time, socket

##############################################################################
# Banner Function
##############################################################################
def banner(ip, port):
    s = socket.socket()

    # The line below will use socket's "connect" method in order to connect to the
    # designated IP address through the designated port.
    s.connect((ip, int(port)))

    # The line below will force the script to stop after five seconds of inactivity.
    s.settimeout(5)

    print(str(s.recv(1024)).strip('b'))
    

##############################################################################
# Main Function
##############################################################################
def main():
    ip = input("Please enter the target's IP address: ")
    port = str(input("Alright, now specify a port: "))
    banner(ip, port)


##############################################################################
# Main
##############################################################################
main()
##############################################################################
# End
##############################################################################