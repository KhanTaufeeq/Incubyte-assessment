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
        result = add_strings('8,9,5,4,3,1002')
        self.assertEqual(result, 29)
    
    def test_add_newline_string(self):
        result = add_strings("1\n2,3\n4")
        self.assertEqual(result, 10)

    def test_add_customised_delimiter_string(self):
        result = add_strings("//*\n1*2")
        self.assertEqual(result, 3)
    
    def test_negative_number_raises_exception(self):
        with self.assertRaises(ValueError) as context:
            add_strings("1, 4, -6, 7")
        
        self.assertIn("Negative numbers not allowed", str(context.exception))
        self.assertIn("-6", str(context.exception))

    def test_multiple_negative_numbers(self):
        with self.assertRaises(ValueError) as context:
            add_strings("1, 4, -6, 7, -3")
        
        self.assertIn("-6", str(context.exception))
        self.assertIn("-3", str(context.exception))

    
    def test_add_multiple_customised_delimiter_string(self):
        result = add_strings("//*\n1******2***3**4")
        self.assertEqual(result, 10)

    def test_add_dual_customised_delimiter_string(self):
        result = add_strings("//*%\n1*2%3")
        self.assertEqual(result, 6)
    

if __name__ == '__main__':
    unittest.main()
