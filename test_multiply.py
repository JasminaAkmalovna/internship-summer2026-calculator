import unittest
from multiply import multiply

class TestMultiply(unittest.TestCase):

    def test_multiply_positive_numbers(self):
        self.assertEqual(multiply(2, 3), 6)

    def test_multiply_negative_numbers(self):
        self.assertEqual(multiply(-2, -3), 6)   
        self.assertEqual(multiply(-2, 3), -6)   

    def test_multiply_by_zero(self):
        self.assertEqual(multiply(5, 0), 0)

    def test_multiply_decimal_numbers(self):
        self.assertEqual(multiply(2.5, 2), 5.0)

if __name__ == '__main__':
    unittest.main()