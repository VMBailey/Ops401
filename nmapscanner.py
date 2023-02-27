#!/usr/bin/python3

# Script Name:      Nmap Scanner
# Author:           Vincent Bailey
# Last Rev:         02/27/2023
# Purpose:          This script will scan a designated IP address using Nmap.
# Source:           https://youtu.be/jYk9XaGoAnk

##############################################################################
# Libraries
##############################################################################
import sys, nmap, time

##############################################################################
# Variables
##############################################################################
# socket.AF_INET tells pythin that we will be creating a socket connection over IPV4.
scanner = nmap.PortScanner()
#target = input

##############################################################################
# Start Menu Function
##############################################################################
def startmenu():
    print("Welcome to our Nmap Automation Tool.")
    print("<---------------------------------------------->")
    time.sleep(1.6)
    target = input("Please enter the IP address you would like to scan: ")
    print("Oooooo good choice. One moment.....")
    time.sleep(1.6)
    print("Alright, so our target is: ", target)
    type(target)

    response = input("Please enter the type of scan you would like to run [1-4]: ")
    print ("1. SYN ACK Scan")
    print ("2. UDP Scan")
    print ("3. Comprehensive Scan")
    print ("4. Exit")
    if response == '1':
        synackscan()
    elif response == '2':
        udpscan()
    elif response == '3':
        compscan()
    elif response == '4':
        print("See you, Space Cowboy")
        time.sleep(1.6)
        sys.exit()
    else:
        print("That's definitely not one of the numbers here. Want to try again?", response)


##############################################################################
# SYN ACK Scan Function
##############################################################################
def synackscan(target):
    print("Nmap Version: ", scanner.nmap_version())

    # this line will run the actual nmap command
    scanner.scan(target, '1-1024', '-V -sS')

    # this will print any of the scan's information to the terminal.
    print(scanner.scaninfo()) 

    # this line will let the user know whether the target IP address is online or offline.
    print("IP Status: ", scanner[target].state())
    print(scanner[target].all_protocols())
    print("Open Ports: ", scanner[target]['tcp'].keys())

##############################################################################
# UDP Scan Function
##############################################################################
def udpscan(target):
    print("Nmap Version: ", scanner.nmap_version())

    # this line will run the actual nmap command
    scanner.scan(target, '1-1024', '-V -sU')

    # this will print any of the scan's information to the terminal.
    print(scanner.scaninfo()) 

    # this line will let the user know whether the target IP address is online or offline.
    print("IP Status: ", scanner[target].state())
    print(scanner[target].all_protocols())
    print("Open Ports: ", scanner[target]['udp'].keys())

##############################################################################
# Comprehensive Scan Function
##############################################################################
def compscan(target):
    print("Nmap Version: ", scanner.nmap_version())

    # this line will run the actual nmap command
    scanner.scan(target, '1-1024', '-V -sS -sV -sC -A -O')

    # this will print any of the scan's information to the terminal.
    print(scanner.scaninfo()) 

    # this line will let the user know whether the target IP address is online or offline.
    print("IP Status: ", scanner[target].state())
    print(scanner[target].all_protocols())
    print("Open Ports: ", scanner[target]['udp'].keys())


##############################################################################
# Main
##############################################################################
startmenu()
##############################################################################
# End
##############################################################################