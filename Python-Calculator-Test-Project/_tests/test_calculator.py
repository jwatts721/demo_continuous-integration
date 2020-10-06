import unittest
import sys
sys.path.append('..')

from lib.calculator import Calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        calc = Calculator()
        self.assertEqual(calc.add(3, 4), 8, "Expected 7")

    def test_subtract(self):
        calc = Calculator()
        self.assertEqual(calc.subtract(10, 7), 3, "Expected 3")

    def test_multiply(self):
        calc = Calculator()
        self.assertEqual(calc.multiply(3, 4), 12, "Expected 12")

    def test_divide(self):
        calc = Calculator()
        self.assertEqual(calc.divide(12, 6), 2, "Expected 2")

if __name__ == '__main__':
    unittest.main()