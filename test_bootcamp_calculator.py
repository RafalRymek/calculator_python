import unittest
from bootcamp_calculator import Calculator


class MyCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_addition_(self):
        self.assertEqual(4, self.calculator.add(2, 2), msg="Wrong calculation result")
        self.assertEqual(6.2, self.calculator.add(4, 2.2), msg="Wrong calculation result")

    def test_subtraction(self):
        self.assertEqual(2, self.calculator.subtract(3,1), msg="Wrong calculation result")
        self.assertEqual(-2, self.calculator.subtract(1,3), msg="Wrong calculation result")

    def test_division(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(3,0)


if __name__ == '__main__':
    unittest.main()