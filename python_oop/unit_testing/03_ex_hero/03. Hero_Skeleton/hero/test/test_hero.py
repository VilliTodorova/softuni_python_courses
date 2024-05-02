from unittest import TestCase, main

from project.hero import Hero


class TestHero(TestCase):

    def setUp(self) -> None:
        self.hero = Hero(
            "test username",
            1,
            100,
            100,
        )
        self.enemy = Hero(
            "enemy test username",
            1,
            50,
            50,
        )

    def test_correct_init(self):
        self.assertEqual("test username", self.hero.username)
        self.assertEqual(10, self.hero.level)
        self.assertEqual(10, self.hero.health)
        self.assertEqual(5, self.hero.damage)

    def test_battle_same_username_error(self):
        self.hero.username = "test"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.hero)

        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_own_hero_health_zero_error(self):
        self.hero.health = 0
        expected = "Your health is lower than or equal to 0. You need to rest"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(expected, str(ex.exception))

    def test_enemy_hero_health_zero_error(self):
        self.enemy.health = 0
        expected = f"You cannot fight enemy test username. He needs to rest"

        with self.assertRaises(Exception) as ex:
            self.hero.battle(self.enemy)

        self.assertEqual(expected, str(ex.exception))

    def test_own_and_enemy_hero_zero_health_draw_reduces_hp(self):
        self.hero.health = 50

        result = self.hero.battle(self.enemy)

        self.assertEqual("Draw", result)
        self.assertEqual(-50, self.enemy.health)
        self.assertEqual(0, self.hero.health)

    def test_enemy_hero_loses(self):
        result = self.hero.battle(self.enemy)

        self.assertEqual("You win", result)
        self.assertEqual(2, self.hero.level)
        self.assertEqual(55, self.hero.health)
        self.assertEqual(105, self.hero.damage)

    def test_own_hero_loses(self):
        self.hero.health = 40
        self.hero.damage = 20

        result = self.hero.battle(self.enemy)

        self.assertEqual("You lose", result)
        self.assertEqual(2, self.enemy.level)
        self.assertEqual(35, self.enemy.health)
        self.assertEqual(55, self.enemy.damage)

    def test_correct_str_representation(self):
        expected = f"Hero test username: 1 lvl\n" \
               f"Health: 100\n" \
               f"Damage: 100\n"

        result = str(self.hero)

        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()