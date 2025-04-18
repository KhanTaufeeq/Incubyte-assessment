import unittest
from calculator import add_strings

class TestStringCalculator(unittest.TestCase):
    def test_add_empty_string(self):
        result = add_strings('')
        self.assertEqual(result, 0)

    def test_add_single_string(self):
        result = add_strings('8')
        self.assertEqual(result, 8)

    def test_add_dual_strings(self):
        result = add_strings('8','9')
        self.assertEqual(result, 17)

    def test_add_multiple_strings(self):
        result = add_strings('8','9','2','5','6')
        self.assertEqual(result, 30)
    
    def test_add_newline_string(self):
        result = add_strings("1\n2,3\n4")
        self.assertEqual(result, 10)
    

if __name__ == '__main__':
    unittest.main()
