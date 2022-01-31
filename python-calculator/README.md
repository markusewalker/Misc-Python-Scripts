# Python Calculator

### Description
Python script that functions as a simple calculator performing addition, subtraction, multiplication and division. Integers and floating point numbers are both accepted in this calculator. The user can specify which operation is performed however many times they wish to and can end the program at any time that they are satisfied.

This script can be ran interactively or silently using command-line arguments. This is further illustrated below.

### Getting Started
To utilize this script in the command-line, please follow the below workflow:

(1) Clone the script into your environment.\
(2) Make sure latest version of Python 3 is installed on the environment.\
(3) Run the script silently: **python3 calculator.py 1 -n1 <number> -n2 <number> -o <operation>**.\
(4) Run the script interactively: **python3 calculator.py 2**

Additionally, this can be ran from your Python IDE of choice such as PyCharm, IDLE, Visual Studio Code, etc.

See below an image of the script in action:
![Image of Calculator](https://github.com/markusewalker/Misc-Python-Scripts/blob/main/python-calculator/calculator.png)

### Testing
Included is `calculator_unittest.py` to check for correctness. The tests provide few, basic tests to verify the addition, subtraction, multiplication and division functions are working properly. To run in the command-line, run the following command:

**python3 -m unittest calculator_unittest.py**
