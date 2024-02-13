from car_manager import Car
from unittest import TestCase, main


class CarTests(TestCase):
    def setUp(self):
        self.car = Car("test", "Renault", 10, 200)

    def test_initialization(self):
        self.assertEqual("test", self.car.make)
        self.assertEqual("Renault", self.car.model)
        self.assertEqual(10, self.car.fuel_consumption)
        self.assertEqual(200, self.car.fuel_capacity)
        self.assertEqual(0, self.car.fuel_amount)

    def test_make_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.make = ""
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_model_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.model = ""
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_fuel_consumption_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_consumption = 0
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_capacity = 0
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_amount_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -5
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_refuel_raises_error_and_ceiling_for_fuel_amount(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))
        self.car.refuel(210)
        self.assertEqual(200, self.car.fuel_amount)

    def test_drive_raises_error(self):
        with self.assertRaises(Exception) as ex:
            self.car.drive(20)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

if __name__ == "__main__":
    main()