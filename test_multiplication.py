import unittest
from divide import divide

class TestDivide(unittest.TestCase):

    def test_divide_positive_numbers(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_decimal_result(self):
        self.assertEqual(divide(7, 2), 3.5)

    def test_divide_negative_numbers(self):
        self.assertEqual(divide(-10, 2), -5)

    def test_divide_by_one(self):
        self.assertEqual(divide(8, 1), 8)
    def test_divide_by_zero(self):

        with self.assertRaises(ZeroDivisionError):
            divide(5, 0)
if __name__ == '__main__':
    unittest.main()