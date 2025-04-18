import unittest
from calculator import add_strings

class TestStringCalculator(unittest.TestCase):
    def TestAddEmptyString(self):
        result = add_strings('')
        self.assertEqual(result, 0)
    

test_case1 = TestStringCalculator()

test_case1.TestAddEmptyString()
