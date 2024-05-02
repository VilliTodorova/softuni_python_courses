from unittest import TestCase, main

from project.mammal import Mammal


class TestMammal(TestCase):

    def setUp(self) -> None:
        self.mammal = Mammal(
            "test name",
            "test type",
            "test sound"
             )

    def test_correct_init_(self):
        self.assertEqual("test name", self.mammal.name)
        self.assertEqual("test type", self.mammal.type)
        self.assertEqual("test sound", self.mammal.sound)
        self.assertEqual("animals", self.mammal._Mammal__kingdom)

    def test_correct_sound(self):
        self.assertEqual("test name makes test sound", self.mammal.make_sound())

    def test_correct_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_correct_info(self):
        self.assertEqual("test name is of type test type", self.mammal.info())


if __name__ == "__main__":
    main()