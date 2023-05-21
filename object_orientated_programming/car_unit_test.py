import unittest

from what_an_interviwer_would_look_at.object_orientated_programming.car import Car


class TestCar(unittest.TestCase):
    def setUp(self):
        self.car = Car("Honda", "Civic", 2015, 50000, 10)

    def test_drive_with_fuel(self):
        self.car.drive(100)
        self.assertEqual(self.car.mileage, 50100)
        self.assertAlmostEqual(self.car.fuel, 5)

    def test_drive_without_fuel(self):
        self.car.fuel = 0
        self.car.drive(100)
        self.assertEqual(self.car.mileage, 50000)
        self.assertEqual(self.car.fuel, 0)


    def test_fill_up(self):
        self.car.fill_up()
        self.assertEqual(self.car.fuel, 15)


if __name__ == '__main__':
    unittest.main()
