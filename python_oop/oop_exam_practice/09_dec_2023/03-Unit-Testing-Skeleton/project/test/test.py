from collections import deque
from unittest import TestCase, main
from project.railway_station import RailwayStation


class TestRailwayStation(TestCase):
    name = "Central"
    arrival_trains = deque()
    departure_trains = deque()

    def setUp(self) -> None:
        self.station = RailwayStation("Central")

    def test_correct_init(self):
        self.assertEqual("Central", self.station.name)
        self.assertEqual(deque(), self.arrival_trains)
        self.assertEqual(deque(), self.departure_trains)

    def test_name_length_equal_to_3_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.station = RailwayStation("Cen")

        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_train_appended_correctly_on_board(self):
        self.station.new_arrival_on_board("Test train")
        self.assertEqual(deque(["Test train"]), self.station.arrival_trains)

    def test_train_has_arrived_other_trains_expected_to_arrive(self):
        self.station.new_arrival_on_board("Test train")
        self.station.new_arrival_on_board("Test train 2")

        self.assertEqual("There are other trains to arrive before Test train 3.",
                         self.station.train_has_arrived("Test train 3"))

    def test_train_has_arrived_correct_pop(self):
        self.station.new_arrival_on_board("Test train")
        self.station.new_arrival_on_board("Test train 2")
        self.station.train_has_arrived("Test train")

        expected = deque(["Test train 2"])
        actual = self.station.arrival_trains

        self.assertEqual(expected, actual)

    def test_train_has_arrived_correct_append_message(self):
        self.station.new_arrival_on_board("Test train")
        self.station.new_arrival_on_board("Test train 2")

        expected = "Test train is on the platform and will leave in 5 minutes."
        actual = self.station.train_has_arrived("Test train")

        self.assertEqual(expected, actual)

    def test_train_has_left_empty_station(self):
        self.station.new_arrival_on_board("")
        self.station.train_has_arrived("")

        actual = self.station.train_has_left("Test train")

        self.assertFalse(actual)

    def test_train_has_left_train_info_false(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.new_arrival_on_board("Test Train2")
        self.station.train_has_arrived("Test Train")
        self.station.train_has_arrived("Test Train2")

        actual = self.station.train_has_left("Test Train2")

        self.assertFalse(actual)

    def test_train_has_left_all_true(self):
        self.station.new_arrival_on_board("Test Train")
        self.station.train_has_arrived("Test Train")

        actual = self.station.train_has_left("Test Train")
        self.assertTrue(actual)


if __name__ == "__main__":
    main()
