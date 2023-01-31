#!/usr/bin/env python3
#
# Authored By:      Markus Walker
# Date Modified:    1/31/23
#
# Description: Unit test for the encrypt-passwords.py script.
import unittest
from encryptpw import *

class TestEncrypt(unittest.TestCase):
    def test_encryption(self):
        self.assertNotEqual(encryption("test"), "b'gAAAAABiItEqE3Kt4bPp0i-7wRP1_4eOlHa3fySmR0sHf7sOrLSBm8_iOVXJAwkfCW1dkTYiXZAcsP5KIxbJsACoCw0eU_sik35WcrJE6MJDujKXSdx939I='")
        self.assertNotEqual(encryption("hello"), "b'gAAAAABiItEqE3Kt4bPp0i-7wRP1_4eOlHa3fySmR0sHf7sOrLSBm8_iOVXJAwkfCW1dkTYiXZAcsP5KIxbJsACoCw0eU_sik35WcrJE6MJDujKXSdx939I='")
        self.assertNotEqual(encryption("yoyo"), "b'gAAAAABiItEqE3Kt4bPp0i-7wRP1_4eOlHa3fySmR0sHf7sOrLSBm8_iOVXJAwkfCW1dkTYiXZAcsP5KIxbJsACoCw0eU_sik35WcrJE6MJDujKXSdx939I='")
    def test_output(self):
        self.assertFalse(output("test", "b'gAAAAABiItEqE3Kt4bPp0i-7wRP1_4eOlHa3fySmR0sHf7sOrLSBm8_iOVXJAwkfCW1dkTYiXZAcsP5KIxbJsACoCw0eU_sik35WcrJE6MJDujKXSdx939I='"))
        
if __name__ == "__main__":
    unittest.main()