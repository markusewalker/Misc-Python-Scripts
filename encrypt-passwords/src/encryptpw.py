#!/usr/bin/env python3
#
# Authored By:      Markus Walker   
# Date Modified:    1/31/23
#
# Description: Encrypts passwords using the Fernet cryptography method.

import argparse, getpass
from cryptography.fernet import Fernet

def encryption(password):
    key = Fernet.generate_key()
    fernet = Fernet(key)

    new_pass = fernet.encrypt(password.encode())

    return new_pass

def output(password, result):
    with open("pass.txt", "w") as text_file:
        print(f"{password}", file=text_file)
        print(f"{result}", file=text_file)
    text_file.close()
    
    print("Key and encrypted password have been saved to pass.txt")

def main():
    parser = argparse.ArgumentParser(description="Encrypts user-inputted passwords using Fernet cryptography")
    parser.add_argument("mode", metavar="mode", type=int, help="runs the script in interactive or silent mode: 1 for silent, 2 for interactive. If silent, run required command-line flags")
    parser.add_argument("-p", "--password", help="password that will be encrypted")

    args = parser.parse_args()

    if args.mode == 1:
        result = encryption(args.password)
        output(args.password, result)
    elif args.mode == 2:
        welcome = """
Welcome to the Encrypt Passwords tool! This will take user-inputted passwords and
encrypt them using the Fernet cryptography method.    
"""
        print(welcome)

        password = getpass.getpass(prompt="Please enter a password that will be used as a key to encrypt: ")
        result = encryption(password)
        output(password, result)

if __name__ == "__main__":
    main()