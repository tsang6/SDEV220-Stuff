import unittest  # Brings in testing tools
from my_sum import sum  # Gets our sum function

class TestSum(unittest.TestCase):  # Creates a test class
    
    def test_list_int(self):  # Our first test
        """
        Test that it can sum a list of integers
        """
        data = [1, 2, 3]  # Make a test list
        result = sum(data)  # Run the function
        self.assertEqual(result, 6)  # Check if answer is 6

if __name__ == '__main__':
    unittest.main()  # Run all tests

    """
My test results indicate success. The dot shows my test case passed. 
"Ran 1 test in 0.000s" tells me it was fast. "OK" confirms everything 
worked as expected. My function properly calculated that 1+2+3 equals 6. 
Automated testing is useful because it checks my code automatically so I 
don't have to do it by hand whenever I make changes.
"""