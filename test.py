import unittest
from calculator import add_strings

class TestStringCalculator(unittest.TestCase):
    def test_add_empty_string(self):
        result = add_strings('')
        self.assertEqual(result, 0)
    

if __name__ == '__main__':
    unittest.main()
