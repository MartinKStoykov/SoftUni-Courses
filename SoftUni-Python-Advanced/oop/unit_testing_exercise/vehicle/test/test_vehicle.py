from project.vehicle import Vehicle
from unittest import TestCase, main

class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(200.0, 150.0)

    def test_initialization(self):
        self.assertEqual(200.0, self.vehicle.fuel)
        self.assertEqual(200.0, self.vehicle.capacity)
        self.assertEqual(150.0, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.fuel_consumption)

    def test_drive_raise_correct_error_and_correct_fuel_decrease(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(1000)
        self.assertEqual("Not enough fuel", str(ex.exception))
        self.vehicle.drive(4)
        self.assertEqual(195.0, self.vehicle.fuel)

    def test_refuel_raise_correct_error_and_correct_fuel_increase(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(250)
        self.assertEqual("Too much fuel", str(ex.exception))
        self.vehicle.fuel = 100
        self.vehicle.refuel(20)
        self.assertEqual(120.0, self.vehicle.fuel)


    def test_str_magic_method_returns_correct_string(self):
        self.assertEqual(f"The vehicle has 150.0 "
                         f"horse power with 200.0 fuel left and 1.25 fuel consumption", self.vehicle.__str__())
if __name__ == "__main__":
    main()