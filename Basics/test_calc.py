import unittest
import simple_calc

"""
I want to test the functions to be sure
that they all working perfectly as I wanted.

To do this, I will use the unittest module.
This module provides a rich set of tools for
constructing and running tests.

"""

class TestCalc(unittest.TestCase):
    """
    Firstly we need to create a class that 
    inherits from unittest.TestCase. 
    """

    def test_evaluate(self):
        result = simple_calc.evaluate("+", 8, -9)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()
