#!/usr/bin/python3

# Script Name:      Attack Tools: Part 2
# Author:           Vincent Bailey
# Last Rev:         12/3/2021
# Purpose:          This script will perform different scans on a target IP address.
# Source:           https://www.pythonpool.com/python-nmap/       

import nmap

scanner = nmap.PortScanner()

print("Nmap Automation Tool")
print("--------------------")

ip_addr = input("IP address to scan: ")
print("The IP you entered is: ", ip_addr)
type(ip_addr)

resp = input("""\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) OS Detection             \n""")
print("You have selected option: ", resp)

range = input("Please enter a desired port range: ")

if resp == '1':
    ### Perfoms a SYN/ACK Scan
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sS')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['tcp'].keys())
elif resp == '2':
    ### Performs a UDP Scan
    print("Nmap Version: ", scanner.nmap_version())
    scanner.scan(ip_addr, range, '-v -sU')
    print(scanner.scaninfo())
    print("Ip Status: ", scanner[ip_addr].state())
    print(scanner[ip_addr].all_protocols())
    print("Open Ports: ", scanner[ip_addr]['udp'].keys())
elif resp == '3':
    ### Detects the target operating system
    print(scanner.scan(ip_addr, arguments="-O")[scanner][ip_addr]['osmatch'][1])
else:
    print("Please enter a valid option")
