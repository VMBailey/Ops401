#!/usr/bin/env python3

# Script Name:      Uptime Sensor Tool
# Author:           Vincent Bailey
# Last Rev:         10/11/2021
# Purpose:          This script will open a menu that will allow a user a choice between
#                   four options revolving around encryption and decryption. 


# Currently following articles and scripts from my classmates to piece this one together. 
# I will resubmit once the script works.

from cryptography.fernet import Fernet

def startmenu():
    print ("1. ENCRYPT a FILE")
    print ("2. DECRYPT a FILE")
    print ("3. ENCRYPT a STRING")
    print ("4. DECRYPT a STRING")
    print ("5. Exit")



startmenu()
choice=input("Select An Option [1-5]:")

if choice==1:
    path=input("Enter Filepath:")
    key=Fernet.generate_key()
    with open('filekey.key', 'wb') as filekey:
        filekey.write(key)
    with open('filekey.key', 'rb'):
        key=filekey.read()
    fernet=Fernet(key)
    with open(path, 'rb') as file:
        original=file.read()
    encrypted=fernet.encrypt(original)
    with open(path, 'wb') as encrypted_file:
        encrypted_file.write(encrypted)