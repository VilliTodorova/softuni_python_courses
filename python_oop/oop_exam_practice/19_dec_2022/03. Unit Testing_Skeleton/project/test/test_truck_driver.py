from unittest import TestCase, main
from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):

    def setUp(self):
        self.driver = TruckDriver("Test", 2.0)

    def test_correct_init(self):
        self.assertEqual("Test", self.driver.name)
        self.assertEqual(2.0, self.driver.money_per_mile)
        self.assertEqual({}, self.driver.available_cargos)
        self.assertEqual(0, self.driver.earned_money)
        self.assertEqual(0, self.driver.miles)

    def test_earned_money_setter_invalid(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1

        self.assertEqual("Test went bankrupt.", str(ve.exception))

    def test_bankrupt(self):
        self.driver.money_per_mile = 0.01
        self.driver.add_cargo_offer("California", 2000)

        with self.assertRaises(ValueError) as ve:
            self.driver.drive_best_cargo_offer()

        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_add_cargo_offer_already_added(self):
        self.driver.add_cargo_offer("Sofia", 200)

        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("Sofia", 200)

        self.assertEqual("Cargo offer is already added.", str(ex.exception))

    def test_add_cargo_offer_valid(self):
        result = self.driver.add_cargo_offer("Sofia", 200)

        self.assertEqual("Cargo for 200 to Sofia was added as an offer.", result)
        self.assertEqual({"Sofia": 200}, self.driver.available_cargos)

    def test_drive_best_cargo_valid(self):
        self.driver.add_cargo_offer("Sofia", 200)
        self.driver.add_cargo_offer("Varna", 100)

        result = self.driver.drive_best_cargo_offer()

        self.assertEqual(f"{self.driver.name} is driving 200 to Sofia.", result)
        self.assertEqual(400, self.driver.earned_money)
        self.assertEqual(200, self.driver.miles)

    def test_drive_best_cargo_invalid(self):
        result = self.driver.drive_best_cargo_offer()

        self.assertEqual("There are no offers available.", result)

    def test_check_for_activities(self):
        self.driver.earned_money = 30_000
        self.driver.check_for_activities(10_000)
        self.assertEqual(self.driver.earned_money, 18250)

    def test_eating(self):
        self.driver.earned_money = 100
        self.driver.eat(249)
        self.driver.eat(250)
        self.driver.eat(500)

        self.assertEqual(60, self.driver.earned_money)

    def test_sleeping(self):
        self.driver.earned_money = 100
        self.driver.sleep(999)
        self.driver.sleep(1000)
        self.driver.sleep(2000)

        self.assertEqual(10, self.driver.earned_money)

    def test_pumping_gas(self):
        self.driver.earned_money = 1000
        self.driver.pump_gas(1499)
        self.driver.pump_gas(1500)
        self.driver.pump_gas(3000)

        self.assertEqual(0, self.driver.earned_money)

    def test_repairing_truck(self):
        self.driver.earned_money = 20_000
        self.driver.repair_truck(9999)
        self.driver.repair_truck(10_000)
        self.driver.repair_truck(20_000)

        self.assertEqual(5000, self.driver.earned_money)

    def test_repr_method(self):
        self.assertEqual("Test has 0 miles behind his back.", str(self.driver))


if __name__ == "__main__":
    main()
