import unittest
import math

from what_an_interviwer_would_look_at.object_orientated_programming.circle import Circle


class TestCircle(unittest.TestCase):
    def setUp(self):
        self.circle = Circle(5)

    def test_area(self):
        self.assertAlmostEqual(self.circle.area(), math.pi * 25)

    def test_circumference(self):
        self.assertAlmostEqual(self.circle.circumference(), math.pi * 10)

if __name__ == "__main__":
    unittest.main()
