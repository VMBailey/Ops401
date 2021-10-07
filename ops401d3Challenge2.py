#!/usr/bin/env python3

# Script Name:      Uptime Sensor Tool
# Author:           Vincent Bailey
# Last Rev:         10/6/2021
# Purpose:          This script will perform a ping request on a specific IP address
#                   until the user stops the program. 

# Import libraries

import os
import sys
import time
import smtplib, ssl
import datetime
from time import gmtime, strftime
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

ip = "8.8.8.8"
response = os.system("ping -c 4 " + ip)
senderAddress='totallyreal@address.com'
senderPass='xxxxxxxxxx'
receiverAddress='totallyreal@address.com'
server_status=1

while True:
    time.sleep(2)
    period = datetime.datetime.now()
    presentTime = strftime("%x %X", gmtime())
    message = MIMEMultipart()
    message['From']=senderAddress
    message['To']=receiverAddress
    message['Subject']='Server Status Change'
    

    if response == 0:
        print (ip, "is up! " + presentTime)
    else:
        print (ip, 'is down! ' + presentTime)

    if response != server_status:
        if response == 0:
            mail_contentup=(ip + " is now AVAILABLE " + presentTime)
            message.attach(MIMEText(mail_contentup, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(senderAddress, senderPass)
            text = message.as_string()
            session.sendmail(senderAddress, receiverAddress, text)
            session.quit()
        else:
            mail_contentdown=(ip + " is now UNAVAILABLE " + presentTime)
            message.attach(MIMEText(mail_contentdown, 'plain'))
            session = smtplib.SMTP('smtp.gmail.com', 587)
            session.starttls()
            session.login(senderAddress, senderPass)
            text = message.as_string() 
            session.sendmail(senderAddress, receiverAddress, text) 
            session.quit()
    server_status=response