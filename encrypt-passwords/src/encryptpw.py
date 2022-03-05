#!/usr/bin/env python3
#
# Authored By:      Markus Walker   
# Date Modified:    3/4/22
#
# Description: Encrypts passwords using the Fernet cryptography method.

import argparse, getpass
from cryptography.fernet import Fernet

# Function to encrypt passwords using Fernet cryptography.
def encryption(password):
    # Instance the Fernet class with the key variable...
    key = Fernet.generate_key()
    fernet = Fernet(key)

    # Encoding to byte string before we can actually encrypt...
    new_pass = fernet.encrypt(password.encode())

    return new_pass

def main():
    parser = argparse.ArgumentParser(description="Encrypts user-inputted passwords using Fernet cryptography")
    parser.add_argument("mode", metavar="mode", type=int, help="runs the script in interactive or silent mode: 1 for silent, 2 for interactive. If silent, run required command-line flags")
    parser.add_argument("-p", "--password", help="password that will be encrypted")

    args = parser.parse_args()

    # If user chooses option 1, run script silently. Else, if user chooses option 2, run script interactively.
    if args.mode == 1:
        # Print out the initial password along with the encrypted password.
        result = encryption(args.password)
        print(f"\nKey: {args.password}")
        print(f"\nEncrypted Password: {result}\n")
    elif args.mode == 2:
        welcome = """
Welcome to the Encrypt Passwords tool! This will take user-inputted passwords and
encrypt them using the Fernet cryptography method.    
"""
        print(welcome)

        # Once password is received, print the key along with the encrypted password.
        password = getpass.getpass(prompt="Please enter a password that will be used as a key to encrypt: ")
        result = encryption(password)
        print(f"\nKey: {password}")
        print(f"\nEncrypted Password: {result}\n")

if __name__ == "__main__":
    main()