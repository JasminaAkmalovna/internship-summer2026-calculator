import unittest
from add2 import add 

class TestAddFunction(unittest.TestCase):
    def test_add_positive_numbers(self):
        self.assertEqual(add(4, 5), 9)

    def test_add_negative_numbers(self):
        self.assertEqual(add(-2, -7), -9)

if __name__ == '__main__':
    unittest.main()