#!/usr/bin/env python3

# Script Name:      File Encryptor
# Author:           Vincent Bailey
# Last Rev:         10/11/2021
# Purpose:          This script will open a menu that will allow a user a choice between
#                   four options revolving around encryption and decryption. 

from cryptography.fernet import Fernet
from posixpath import dirname
import time
import os

def startmenu():       
    print ("1. File Encryption")
    print ("2. File Decryption")
    print ("3. Message Encryption")
    print ("4. Message Decryption")
    print ("5. Get Out!!")

def encrypt(fileName):
    key = load_key()
    """
    Given a fileLocation (str) and key (bytes), it encrypts the file.
    """
    f = Fernet(key)
    fileName = input("Alright cool. Input the file name that you wish to encrypt: ")
    with open(fileName, "rb") as file:
        # read all file data
        file_data = file.read()
    # encrypt data
    encrypted_data = f.encrypt(file_data)
    # write the encrypted file
    with open(fileName, "wb") as encrypted_file:
        encrypted_file.write(encrypted_data)
    file.close()
    encrypted_file.close()

def decrypt(fileName): 
    """
    Given a fileLocation (str) and key (bytes), it decrypts the file.
    """
    key = load_key()
    f = Fernet(key)
    fileName = input("Alright cool. Input the file name that you wish to decrypt: ")
    with open(fileName, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(fileName, "wb") as file:
        file.write(decrypted_data)

def encrypt_message(message):
    """
    Encrypts a message
    """
    key = load_key()
    encoded_message = message.encode()
    f = Fernet(key)
    encrypted_message = f.encrypt(encoded_message)

    print(encrypted_message)

def decrypt_message(message):
    """
    Decrypts an encrypted message
    """
    decrypted_message=message.encode()
    key = load_key()
    f = Fernet(key)
    message = f.decrypt(message)
    
    print(message)

def generate_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
        return key

def load_key():
    """
    Load the previously generated key
    """
    return open("key.key", "rb").read()

def main():
    startmenu()
    selection = '0'
    loop = True
    while loop:
        selection = input("Enter Your Numbered Choice [1-5]: " )
        
        if selection == "1":
            encrypt()
            print ("Menu 1 has been selected")
        elif selection==2:
            decrypt()
            print ("Menu 2 has been selected")
        elif selection == "3":
            encrypt_message()
            print ("Menu 3 has been selected")
        elif selection==4:
            decrypt_message()
            print ("Menu 4 has been selected")
        elif selection == "5":
            print ("See ya!!")
            exit(0)
        else:
            print ("Umm......pretty sure that's not one of the numbers listed...wanna try again?")
            startmenu()


main()