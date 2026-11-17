import unittest
from calculator import *

class TestCalculator(unittest.TestCase):
    ######### Partner 2
    def test_add(self):
        self.assertEqual(add(2,3),5)
        self.assertEqual(add(-4,7),3)
        self.assertEqual(add(0,0),0)

    def test_subtract(self): # 3 assertions
        self.assertEqual(subtract(10,3),7)
        self.assertEqual(subtract(3, 10), -7)
        self.assertEqual(subtract(-5, -2), -3)
    # ##########################

    def test_multiply(self):
        self.assertEqual(multiply(3, 4), 12)
        self.assertEqual(multiply(-2, 5), -10)
        self.assertEqual(multiply(0, 100), 0)

    def test_divide(self):
        self.assertAlmostEqual(divide(10, 2), 5.0)
        self.assertAlmostEqual(divide(7, 2), 3.5)
        self.assertAlmostEqual(divide(-9, 3), -3.0)

    ######## Partner 2
    def test_divide_by_zero(self): # 1 assertion
        with self.assertRaises(ZeroDivisionError):
            div(0, 5)

    def test_logarithm(self): # 3 assertions
        self.assertAlmostEqual(logarithm(2,8),3)
        self.assertAlmostEqual(logarithm(10, 100), 2)
        self.assertAlmostEqual(logarithm(0.5, 4), -2)

    def test_log_invalid_base(self): # 1 assertion
        with self.assertRaises(ValueError):
            logarithm(1,10)

    ######## Partner 1
    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(-3, -4), 5.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(9), 3.0)
        self.assertAlmostEqual(square_root(2), math.sqrt(2))
        self.assertAlmostEqual(square_root(0), 0.0)

# Do not touch this
if __name__ == "__main__":
    unittest.main()
