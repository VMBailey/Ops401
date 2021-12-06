# Script Name:      Web Application Fingerprinting Tool
# Author:           Vincent Bailey
# Last Rev:         11/23/2021
# Purpose:          This script will scan a designated address and port using
#                   netcat, telnet, or nmap. 

##############################################################################
# Import Library 
##############################################################################
import os, sys, time

##############################################################################
# Start Menu Function
##############################################################################
def startmenu():
    print ("1. NETCAT")
    print ("2. TELNET")
    print ("3. NMAP")
    print ("4. Exit")
    selection = input("Enter Your Numbered Choice [1-5]: " )
    if selection == '1':
        netcat()
    elif selection == '2':
        telnet()
    elif selection == '3':
        nmap()
    elif selection == '4':
        print("See you, Space Cowboy")
        time.sleep(1.6)
        sys.exit()
    else:
        print("That's definitely not one of the numbers here. Want to try again?")
    return selection

##############################################################################
# Destination
##############################################################################
def address():
    place = input("Please enter a target: ")
    return place

##############################################################################
# Port
##############################################################################
def port():
    targetport = input("Please enter a port number: ")
    return targetport

##############################################################################
# NetCat
##############################################################################
def netcat():
    catrun=("nc -N " +  address() + ' '+ port())
    return os.system(catrun)

##############################################################################
# TelNet
##############################################################################
def telnet():
    telrun=("telnet " +  address() + ' '+ port())
    return os.system(telrun)

##############################################################################
# NMap
##############################################################################
def nmap():
    # By default, nmap will scan 1,000 of the most common ports.
    # To narrow this down in the future, use "-F" for a fast scan. This will
    # bring the search down to 100 ports.
    maprun=("nmap " + address())
    return os.system(maprun)

##############################################################################
# Main
##############################################################################
startmenu()
##############################################################################
# End
##############################################################################
