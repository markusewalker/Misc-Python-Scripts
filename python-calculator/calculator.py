#!/usr/bin/env python

# Authored By: Markus Walker
# Date Modified: 1/28/22
#
# Descrption: Simple calculator written in Python 3. It provides the following
# operations:
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
import argparse

# This function adds two numbers
def addition(x, y):
    return x + y

# This function subtracts two numbers
def subtraction(x, y):
    return x - y

# This function multiplies two numbers
def multiplication(x, y):
    return x * y

# This function divides two numbers
def division(x, y):
    return x / y

def main():
    welcome = """
Welcome to the Simple Python Calculator! Please find the below supported operations:
 
    1. Addition
    2. Subtraction
    3. Multiplication
    4. Division

To keep it simple, this calculator takes only two numbers as input.
    """
    print(welcome)

    # While loop that will check the user input for the calculator and reference appropriate function.
    while True:
        choice = input("Please enter the operation you wish to perform: ")

        # Must choose a number in the range of 1-4....if not, it will throw an error.
        if choice in ("1", "2", "3", "4"):
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

            # Ask if the user wishes to continue performing calculations; end if they do not.
            next_choice = input("Would you like to continue? Enter 'yes' or 'no': ")
            if next_choice == "yes":
                continue
            elif next_choice == "no":
                break
            else:
                print("Huh? Ending the program...")
                break
        else:
            print("ERROR. You must choose a number in the range 1-4. Please try again...")

if __name__ == "__main__":
    main()