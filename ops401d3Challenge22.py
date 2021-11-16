# Script Name:      Signature-based Malware Detection Tool
# Author:           Vincent Bailey
# Last Rev:         11/15/2021
# Purpose:          This script will hunt for a file in a directory designated by the user.

import time, os

def main():
    print ("Hey there! What file are you looking for?")
    time.sleep(1.6)
    file = input("Enter the file's name and extension here: ")

    print ("Cool. Where should I look?")
    time.sleep(1.6)
    directory = input ("Enter a directory name: ")

    os.chdir(directory)

main()

"""
    This script is not complete yet. It switches to the designated directory, but I need to figure out how to
    make it display its search results and let the user know that the file has been found or not.
"""
