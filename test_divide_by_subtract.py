import unittest
from divide_by_subtract import divide

class TestDivideBySubtract(unittest.TestCase):

    def test_divide_positive(self):
        self.assertEqual(divide(10, 2), 5)

    def test_divide_decimal(self):
        self.assertEqual(divide(5, 2), 2.5)

    def test_divide_negative(self):
        self.assertEqual(divide(-10, 2), -5)   

    def test_divide_zero_by_number(self):
        self.assertEqual(divide(0, 5), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            divide(10, 0)

    def test_divide_string(self):
        with self.assertRaises(TypeError):
            divide("10", 2)

if __name__ == '__main__':
    unittest.main()