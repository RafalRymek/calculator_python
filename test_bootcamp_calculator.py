import unittest
from bootcamp_calculator import Calculator


class MyCalculatorTest(unittest.TestCase):

    def setUp(self):
        self.calculator = Calculator()

    def test_add_two_positive_int(self):
        self.assertEqual(4, self.calculator.add(2, 2), msg="Wrong calculation result")

    def test_add_two_positive_int_and_float(self):
        self.assertEqual(6.2, self.calculator.add(4, 2.2), msg="Wrong calculation result")

    def test_add_two_negative_int(self):
        self.assertEqual(-4, self.calculator.add(-2, -2), msg="Wrong calculation result")

    def test_add_two_negative_int_and_float(self):
        self.assertEqual(-6.2, self.calculator.add(-4, -2.2), msg="Wrong calculation result")

    def test_subtract_two_positive_int(self):
        self.assertEqual(2, self.calculator.subtract(3,1), msg="Wrong calculation result")

    def test_subtract_two_positive_int_and_float(self):
        self.assertEqual(0.0, self.calculator.subtract(3, 3.0), msg="Wrong calculation result")

    def test_subtract_two_negative_int(self):
        self.assertEqual(0, self.calculator.subtract(-2, -2), msg="Wrong calculation result")

    def test_subtract_two_negative_int_and_float(self):
        self.assertEqual(-2.0, self.calculator.subtract(-4, -2.0), msg="Wrong calculation result")

    def test_multiply_two_positive_int(self):
        self.assertEqual(3, self.calculator.multiply(3, 1), msg="Wrong calculation result")

    def test_multiply_two_positive_int_and_float(self):
        self.assertEqual(9.0, self.calculator.multiply(3, 3.0), msg="Wrong calculation result")

    def test_multiply_two_negative_int(self):
        self.assertEqual(4, self.calculator.multiply(-2, -2), msg="Wrong calculation result")

    def test_multiply_two_negative_int_and_float(self):
        self.assertEqual(8.0, self.calculator.multiply(-4, -2.0), msg="Wrong calculation result")

    def test_divide_two_positive_int(self):
        self.assertEqual(3, self.calculator.divide(3, 1), msg="Wrong calculation result")

    def test_divide_two_positive_int_and_float(self):
        self.assertEqual(1.0, self.calculator.divide(3, 3.0), msg="Wrong calculation result")

    def test_divide_two_negative_int(self):
        self.assertEqual(1, self.calculator.divide(-2, -2), msg="Wrong calculation result")

    def test_divide_two_negative_int_and_float(self):
        self.assertEqual(2.0, self.calculator.divide(-4, -2.0), msg="Wrong calculation result")

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            self.calculator.divide(3, 0)

    def test_add_empty_input(self):
        self.assertIsNotNone(self.calculator.add(None, 5))

    def test_add_very_long_numbers(self):
        self.assertEqual(342777279687577658876874768858768869877799890690, self.calculator.add(
            432134234123423423423423423423434532454545345, 342345145453454235453451345435345435345345345345))

    def test_input_letter_than_number(self):
        with self.assertRaises(TypeError):
            self.calculator.add("a", 5)


if __name__ == '__main__':
    unittest.main()