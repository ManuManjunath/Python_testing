import unittest
from calculator import Calculator

class CalculatorTest(unittest.TestCase):

    def test_add(self):
        addition = Calculator.add(10, -2)
        self.assertEqual(addition, 8)

    def test_subtract(self):
        subtraction = Calculator.subtract(10, -2)
        self.assertEqual(subtraction, 12)

    def test_multiply(self):
        multiplication = Calculator.multiply(10, -2)
        self.assertEqual(multiplication, -20)

    def test_divide(self):
        division = Calculator.divide(10, 0)
        self.assertEqual(division, "Error: Cannot divide by 0")
