#!/usr/bin/env python

# Authored By: Markus Walker
# Date Modified: 1/30/22
#
# Descrption: Unit test for the calculator.py script. Several unit tests 
# against the addition, subtraction, multiplication and division functions
# of the calculator.py script.
from calculator import *
import unittest
from unittest.mock import patch

class TestCalculator(unittest.TestCase):
    def test_addition(self):
        self.assertEqual(addition(20,10), 30.0)
        self.assertNotEqual(addition(20,10), 10.0)
    
    def test_subtraction(self):
        self.assertEqual(subtraction(20,10), 10.0)
        self.assertNotEqual(subtraction(20,10), 30.0)

    def test_multiplication(self):
        self.assertEqual(multiplication(20,10), 200.0)
        self.assertNotEqual(multiplication(20,10), 2.0)

    def test_division(self):
        self.assertEqual(division(20,10), 2.0)
        self.assertNotEqual(division(20,10), 200.0)

if __name__ == "__main__":
    unittest.main()