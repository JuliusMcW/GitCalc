import example
import unittest


class Tester(unittest.TestCase):
    def test_add(self):
        result = example.addition(0, 1)
        self.assertEqual(result, 1)

    def test_subtract(self):
        result = example.subtraction(4, 2)
        self.assertEqual(result, 2)

    def test_mul(self):
        result = example.multiplication(1, 3)
        self.assertEqual(result, 3)

    def test_division(self):
        result = example.division(20, 5)
        self.assertEqual(result, 4)
