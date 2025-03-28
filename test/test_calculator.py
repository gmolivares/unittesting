import unittest
from src.calculator import sum,subtract,multiply,div


class CalculatorTests(unittest.TestCase):
    
    def test_sum(self):
        assert sum(2,3)== 5
    
    def test_subtract(self):
        assert subtract(10,5)==5

    def test_multiply(self):
        assert multiply(5,5)==25

    def test_div(self):
        assert div(5,1)==5
    
    def test_div_cero(self):
        with self.assertRaises(ValueError) as context:
            div(5, 0)