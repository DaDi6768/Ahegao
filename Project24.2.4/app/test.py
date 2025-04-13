import pytest
from app.Calc import Calculator

class TestCalc:
    def setup(self):
        self.Calc = Calculator


    def test_multiply(self):
        assert self.Calc.multiply(self,5,5) == 25

    def test_division(self):
        assert  self.Calc.division(self,3,3) == 1

    def test_subtraction(self):
        assert self.Calc.subtraction(self,7,3) == 4

    def test_adding(self):
        assert self.Calc.adding(self,5,5) == 10