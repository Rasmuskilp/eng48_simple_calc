import unittest
from simple_calc import SimpleCalc

class Calctest(unittest.TestCase):
    calc = SimpleCalc()
    def test_add(self):
        self.assertEqual(self.calc.add(2,4),6)
        self.assertEqual(self.calc.add(5,4),9)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(4,2),2)
        self.assertEqual(self.calc.subtract(8,4),4)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(5,6),30)
        self.assertEqual(self.calc.multiply(2,3),6)

    def test_divide(self):
        self.assertEqual(self.calc.divide(16,4),4)
        self.assertEqual(self.calc.divide(8,4),2)
    def test_add2(self):
        self.assertEqual(self.calc.add(3,5),8)
