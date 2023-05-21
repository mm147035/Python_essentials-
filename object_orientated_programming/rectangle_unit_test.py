import unittest
from what_an_interviwer_would_look_at.object_orientated_programming.rectangle import Rectangle


class TestRectangle(unittest.TestCase):
    def test_area(self):
        # Test case for calculating the area of the rectangle
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.area(), 50)

    def test_perimeter(self):
        # Test case for calculating the perimeter of the rectangle
        rectangle = Rectangle(5, 10)
        self.assertEqual(rectangle.perimeter(), 30)

if __name__ == '__main__':
    unittest.main()