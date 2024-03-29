#!/usr/bin/env python3

# Authored By: Markus Walker
# Date Modified: 1/31/23
#
# Descrption: Calculator written in Python 3. It provides the following operations:
# addition, subtraction, multiplication, division, remainder, squared, cubed.

import argparse

def addition(x, y):
    return x + y

def subtraction(x, y):
    return x - y

def multiplication(x, y):
    return x * y

def division(x, y):
    return x / y

def remainder(x, y):
    return x % y

def squared(x, y):
    return x ** y

def cubed(x, y):
    return (x ** y) * x

def interactive():
    welcome = """
Welcome to the Python Calculator! Please find the below supported operations:

    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division
    5. Remainder
    6. Squared
    7. Cubed

To keep it simple, this calculator takes only two numbers as input.
"""
    print(welcome)

    while True:
        choice = input("Please enter the operation you wish to perform: ")

        if choice in ("1", "2", "3", "4", "5", "6", "7"):
            num1 = float(input("Please enter the first number: "))
            num2 = float(input("Please enter the second number: "))

            if choice == "1":
                print(f"{num1} + {num2} =", addition(num1, num2))
            elif choice == "2":
                print(f"{num1} - {num2} =", subtraction(num1, num2))
            elif choice == "3":
                print(f"{num1} * {num2} =", multiplication(num1, num2))
            elif choice == "4":
                print(f"{num1} / {num2} =", division(num1, num2))
            elif choice == "5":
                print(f"{num1} % {num2} =", remainder(num1, num2))
            elif choice == "6":
                print(f"{num1} ** {num2} =", squared(num1, num2))
            elif choice == "7":
                print(f"{num1} ** {num2} * {num1} =", cubed(num1, num2))

            next_choice = input("\nWould you like to continue? Enter 'yes'|'y' or 'no'|'n': ")
            while next_choice not in ("yes", "y", "no", "n"):
                next_choice = input("Please enter 'yes'|'y' or 'no'|'n': ")
            if next_choice == "yes" or next_choice == "y":
                continue
            elif next_choice == "no" or next_choice == "n":
                print("Thank you for using the Python Calculator!")
                break
        else:
            print("You must choose a number in the range 1-7. Please try again...\n")
            continue

def main():
    parser = argparse.ArgumentParser(description="Performs the following operations: addition, subtraction, multiplication, division, remainder, squared, cubed.")
    parser.add_argument('mode', metavar='mode', type=int, help="runs the script in interactive or silent mode: 1 for silent, 2 for interactive. If silent, run the other command-line flags as well.")
    parser.add_argument("-n1", "--number1", type=int, help="first number to input")
    parser.add_argument("-n2", "--number2", type=int, help="second number to input")
    parser.add_argument("-o", "--operation", type=str, help="operation to perform: add, sub, mult, div, rem, squ, cub")

    args = parser.parse_args()
    num1 = args.number1
    num2 = args.number2

    if args.mode == 1:
        if args.operation == "add":
            print(f"{num1} + {num2} =", addition(num1, num2))
        elif args.operation == "sub":
            print(f"{num1} - {num2} =", subtraction(num1, num2))
        elif args.operation == "mult":
            print(f"{num1} * {num2} =", multiplication(num1, num2))
        elif args.operation == "div":
            print(f"{num1} / {num2} =", division(num1, num2))
        elif args.operation == "rem":
            print(f"{num1} % {num2} =", remainder(num1, num2))
        elif args.operation == "squ":
            print(f"{num1} ** {num2} =", squared(num1, num2))
        elif args.operation == "cub":
            print(f"{num1} ** {num2} * {num1} =", cubed(num1, num2))
    elif args.mode == 2:
        interactive()
    else:
        print("ERROR. Supported operations are 1 or 2. Please try again.")

if __name__ == "__main__":
    main()
