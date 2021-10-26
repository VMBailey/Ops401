#!/usr/bin/env python3

# Script Name:      Automated Brute Force Wordlist Attack Tool
# Author:           Vincent Bailey
# Last Rev:         10/25/2021
# Purpose:          This script will use word lists to search for passwords.

import sys, time, requests

def startmenu():
    print ("1. Offensive: Dictionary Iterator")
    print ("2. Defensive: Password Search")
    print ("3. Exit")
    selection = input("Enter Your Numbered Choice [1-3]: " )
    if selection == '1':
        offense()
    elif selection == '2':
        defense()
    elif selection == '3':
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
    # While loop to set delay
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

startmenu()