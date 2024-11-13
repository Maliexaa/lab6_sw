import unittest
from SquareCalculator import SquareCalculator  # Import the correct class

class TestSquareCalculator(unittest.TestCase):

    def setUp(self):
        # This method is run before each test, useful for setup code.
        self.calc = SquareCalculator()

    def test_area(self):
        # Test area calculation
        result = self.calc.area(3)
        self.assertEqual(result, 9)
        
    def test_perimeter(self):
        # Test perimeter calculation
        result = self.calc.perimeter(3)
        self.assertEqual(result, 12)

if __name__ == '__main__':
    unittest.main()
