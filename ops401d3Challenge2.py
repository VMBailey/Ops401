#!/usr/bin/env python3

# Script Name:      Uptime Sensor Tool
# Author:           Vincent Bailey
# Last Rev:         10/5/2021
# Purpose:          This script will perform a ping request on a specific IP address
#                   until the user stops the program.

# Import libraries

import os
import sys
import time
import datetime
from time import gmtime, strftime

ip = "8.8.8.8"
response = os.system("ping -c 1" + ip)

while True:
    time.sleep(2)
    period = datetime.datetime.now()
    presentTime=strftime("%x %X", gmtime())
    if response == 0:
        print (ip, "is up! " + presentTime)
    else:
        print (ip, 'is down! ' + presentTime)
