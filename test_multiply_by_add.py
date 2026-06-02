import unittest
from multiply2 import multiply_by_add 

class TestMultiplyByAdd(unittest.TestCase):
    def test_multiply_positive_numbers(self):
        # 5 * 3 = 15 (adding 5 three times)
        self.assertEqual(multiply_by_add(5, 3), 15)

    def test_multiply_by_zero(self):
        self.assertEqual(multiply_by_add(5, 0), 0)

    def test_multiply_by_one(self):
        self.assertEqual(multiply_by_add(7, 1), 7)

if __name__ == '__main__':
    unittest.main()