# Encrypt Passwords

### Description
Python script that will encrypt user-inputted passwords using the Fernet cryptography method. Fernet is a symmetric encryption method
that is builtin to the `cryptography` package, so you will need to install it. You can simply do the following:

`pip3 install cryptography`

This script can be ran interactively or silently, see the below to see how.

### Getting Started
To utilize this script in the command-line, please follow the below workflow:

(1) Clone the script into your environment.\
(2) Make sure latest version of Python 3 is installed on the environment.\
(3) Run the script interactively: `python3 encryptpw.py 1 -p <password>`.\
(4) Run the script interactively: `python3 encryptpw.py 2`.

Additionally, this can be ran from your Python IDE of choice such as PyCharm, IDLE, Visual Studio Code, etc.

See below an image of the script in action:
![Example](https://github.com/markusewalker/Misc-Python-Scripts/blob/main/encrypt-passwords/example.jpg)

### Testing
Included is `encryptpw_unittest.py` to check for correctness. The tests provide few, basic tests to verify the addition, subtraction, multiplication and division functions are working properly. To run in the command-line, run the following command:

`python3 -m unittest encryptpw_unittest.py`
