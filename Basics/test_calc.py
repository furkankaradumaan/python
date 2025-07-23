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

    def test_evaluate_sum(self):

        self.assertEqual(simple_calc.evaluate("+", 8, -9), -1)
        self.assertEqual(simple_calc.evaluate("+", 1, 10), 11)
        self.assertEqual(simple_calc.evaluate("+", -5, -123), -128)
        self.assertEqual(simple_calc.evaluate("+", 0, 12), 12)

    def test_evaluate_sub(self):
        
        self.assertEqual(simple_calc.evaluate("-", 12, 4), 8)
        self.assertEqual(simple_calc.evaluate("-", 14, -11), 25)
        self.assertEqual(simple_calc.evaluate("-", -23, -4), -19)
        self.assertEqual(simple_calc.evaluate("-", 0, 6), -6)
        self.assertEqual(simple_calc.evaluate("-", 0, -11), 11)
        self.assertEqual(simple_calc.evaluate("-", 8, 0), 8)
    
    def test_evaluate_mul(self):
        
        self.assertEqual(simple_calc.evaluate("*", 9, 4), 36)
        self.assertEqual(simple_calc.evaluate("*", -1, -11), 11)
        self.assertEqual(simple_calc.evaluate("*", -12, 4), -48)
        self.assertEqual(simple_calc.evaluate("*", 0, 12), 0)
        
        with self.assertRaises(ArithmeticError):
            simple_calc.evaluate("*", 0, 0)

    def test_evaluate_div(self):
        
        self.assertEqual(simple_calc.evaluate("/", 4, 6), (4/6))
        self.assertEqual(simple_calc.evaluate("/", 9, 3), 3.0)
        self.assertEqual(simple_calc.evaluate("/", 6, 1), 6.0)
        self.assertEqual(simple_calc.evaluate("/", -12, -6), 2.0)
        self.assertEqual(simple_calc.evaluate("/", -6, 5), (-6/5))
        self.assertEqual(simple_calc.evaluate("/", 0, 12), 0)
        self.assertRaises(ZeroDivisionError, simple_calc.evaluate, "/", -6, 0)
    

if __name__ == "__main__":
    unittest.main()
