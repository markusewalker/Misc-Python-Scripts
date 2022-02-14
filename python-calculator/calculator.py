#!/usr/bin/env python3

# Authored By: Markus Walker
# Date Modified: 2/13/22
#
# Descrption: Calculator written in Python 3. It provides the following
# operations:
#   1. Addition
#   2. Subtraction
#   3. Multiplication
#   4. Division
#   5. Remainder
#   6. Squared
#   7. Cubed
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

# Function to interactively run the script if the user chose option 2.
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

    # While loop that will check the user input for the calculator and reference appropriate function.
    while True:
        choice = input("Please enter the operation you wish to perform: ")

        # Must choose a number in the range of 1-6....if not, it will throw an error.
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
            print("ERROR. You must choose a number in the range 1-7. Please try again...")

def main():
    parser = argparse.ArgumentParser(description="Performs the following operations: addition, subtraction, multiplication, division, remainder, squared, cubed.")
    parser.add_argument('mode', metavar='mode', type=int, help="runs the script in interactive or silent mode: 1 for silent, 2 for interactive. If interactive, run the other command-line flags as well.")
    parser.add_argument("-n1", "--number1", type=int, help="first number to input")
    parser.add_argument("-n2", "--number2", type=int, help="second number to input")
    parser.add_argument("-o", "--operation", help="operation to perform: 'add', 'sub', 'mult', 'div', 'rem', 'squ', 'cube'")

    # Read in the above arguments and assign num1 and num2 to the user inputted numbers. 
    args = parser.parse_args()
    num1 = args.number1
    num2 = args.number2

    # If user chooses option 1, then run in silent mode.
    if args.mode == 1:
        # Depending on operation chose, perform the respective calculation with the two numbers.
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
    # If user chooses option 2, then run in interactive mode.
    elif args.mode == 2:
        interactive()
    else:
        print("ERROR. Supported operations are 1 or 2. Please try again.")

if __name__ == "__main__":
    main()
