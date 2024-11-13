import unittest
from calculator import SquareCalculator

class TestSquareCalculator(unittest.TestCase): 

    def setUp(self):
        
        self.calc = SquareCalculator()

    def test_area(self):
        result = self.calc.area(3)
        self.assertEqual(result, 9)

    def test_perimeter(self):
        result = self.calc.perimeter(3)
        self.assertEqual(result, 12) 
if __name__ == "__main__":
    unittest.main()
