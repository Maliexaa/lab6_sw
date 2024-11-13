# test_square_calculator.py
import unittest
from square_calculator import SquareCalculator

class TestSquareCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = SquareCalculator()

    def test_area(self):
        # Test area method for the square
        result = self.calc.area(3)
        self.assertEqual(result, 9)

        result = self.calc.area(0)
        self.assertEqual(result, 0)

        result = self.calc.area(-1)
        self.assertEqual(result, 1) 

    def test_perimeter(self):
        # Test perimeter method for the square
        result = self.calc.perimeter(3)
        self.assertEqual(result, 12)

        result = self.calc.perimeter(0)
        self.assertEqual(result, 0) 
        result = self.calc.perimeter(-1)
        self.assertEqual(result, -4)  # -1 * 4 = -4 (assuming negative side length is allowed)

if __name__ == "__main__":
    unittest.main()
