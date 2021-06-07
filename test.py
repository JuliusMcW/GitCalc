import example
import unittest


class Tester(unittest.TestCase):
    def test_add(self):
        result = calc.addition(0, 1)
        self.assertEqual(result, 1)

    def test_subtract(self):
        result = calc.subtraction(4, 2)
        self.assertEqual(result, 2)

    def test_mul(self):
        result = calc.multiplication(1, 3)
        self.assertEqual(result, 3)

    def test_division(self):
        result = calc.division(20, 5)
        self.assertEqual(result, 4)
