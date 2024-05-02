from unittest import TestCase, main

from project.vehicle import Vehicle


class TestVehicle(TestCase):

    def setUp(self) -> None:
        self.vehicle = Vehicle(
            50,
            50,
        )

    def test_default_fuel_consumption_correct(self):
        self.assertEqual(1.25, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_correct_init(self):
        self.assertEqual(50, self.vehicle.fuel)
        self.assertEqual(50, self.vehicle.horse_power)
        self.assertEqual(50, self.vehicle.capacity)
        self.assertEqual(self.vehicle.fuel_consumption, Vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_driving_calculating_correct_fuel(self):
        self.vehicle.drive(10)

        self.assertEqual(37.5, self.vehicle.fuel)

    def test_driving_not_enough_fuel(self):
        self.vehicle.fuel = 0

        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)

        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_refueling_correct(self):
        self.vehicle.fuel = 0
        self.vehicle.refuel(40)

        self.assertEqual(40, self.vehicle.fuel)

    def test_refueling_overfill(self):
        self.vehicle.fuel = 50

        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(10)

        self.assertEqual("Too much fuel", str(ex.exception))

    def test_correct_string_representation(self):
        expected = "The vehicle has 50 horse power with 50 fuel left and 1.25 fuel consumption"
        self.assertEqual(expected, str(self.vehicle))


if __name__ == "__main__":
    main()
