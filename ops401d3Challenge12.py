#!/usr/bin/env python3

# Script Name:      Network Security Tool
# Author:           Vincent Bailey
# Last Rev:         10/19/2021
# Purpose:          This script will scan a designated network declared by the user.

# Library Imports
from ipaddress import IPv4Network
import ipaddress
from scapy.all import ICMP, IP, sr1, TCP
import random

# Define end target and TCP port range
target = "192.168.40.1"
portRange = [22, 23, 80, 443, 3389]

## Your menu design here
def startmenu():  
    print ("1. TCP Port Range Scanner")
    print ("2. ICMP Ping Sweep Mode")
    selection = input("Enter Your Numbered Choice [1-2]: " )
    if selection == '1':
        getTCP()
    elif selection == '2':
        getICMP()
    return selection


def getICMP():
    proceed = False
    while proceed == False:
        cidrAddress = input("Enter a valid CIDR block: ") or "10.0.0.0/24"
        try:
            ipList = ipaddress.ip_network(cidrAddress)
            return ipList
        except:
            print("Pretty sure that's not a valid CIDR block. Please try again.")


## Send SYN with random Src Port for each Dst port
def getTCP():
    for dst_port in portRange:
        src_port = random.randint(1025,65534)
    resp = sr1(
        IP(dst=target)/TCP(sport=src_port,dport=dst_port,flags="S"),timeout=1,
        verbose=0,
    )
    """
    # Try to figure out how to get the responding packets in terminal
    packet = resp
    packet.show()
    """
    
    if resp is None:
        print(f"{target}:{dst_port} is filtered (silently dropped).")

    elif(resp.haslayer(TCP)):
        if(resp.getlayer(TCP).flags == 0x12):
            # Send a gratuitous RST to close the connection
            send_rst = sr1(
                IP(dst=target)/TCP(sport=src_port,dport=dst_port,flags='R'),
                timeout=1,
                verbose=0,
            )
            print(f"{target}:{dst_port} is open.")

        elif (resp.getlayer(TCP).flags == 0x14):
            print(f"{target}:{dst_port} is closed.")
     
    # This line is reserved for today's challenge
    elif(resp.haslayer(ICMP)):
        if(
            int(resp.getlayer(ICMP).type) == 3 and
            int(resp.getlayer(ICMP).code) in [1,2,3,9,10,13]
        ):
            print(f"{target}:{dst_port} is filtered (silently dropped).")
    
startmenu()