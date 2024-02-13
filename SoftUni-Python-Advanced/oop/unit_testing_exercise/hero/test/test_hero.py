from project.hero import Hero
from unittest import TestCase, main

class HeroTest(TestCase):
    def setUp(self):
        self.hero = Hero("Link", 64, 80, 10)
        self.enemy_hero = Hero("Ganondorf", 80, 200, 12)
    def test_initialization(self):
        self.assertEqual("Link", self.hero.username)
        self.assertEqual(64, self.hero.level)
        self.assertEqual(80, self.hero.health)
        self.assertEqual(10, self.hero.damage)

    def test_battle_battle_username(self):
        with self.assertRaises(Exception) as ex:
            self.enemy_hero.name = "Link"
            self.hero.battle(self.hero)
        self.assertEqual("You cannot fight yourself", str(ex.exception))

    def test_battle_hero_health_above_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual("Your health is lower than or equal to 0. You need to rest", str(ve.exception))

    def test_battle_enemy_hero_below_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.enemy_hero.health = 0
            self.hero.battle(self.enemy_hero)
        self.assertEqual("You cannot fight Ganondorf. He needs to rest", str(ve.exception))

    def test_battle_result_is_draw(self):
        self.hero.health = 20
        self.enemy_hero. health = 10
        self.assertEqual("Draw", self.hero.battle(self.enemy_hero))

    def test_battle_result_is_victory(self):
        self.enemy_hero.level = 1
        self.assertEqual("You win", self.hero.battle(self.enemy_hero))
        self.assertEqual(65, self.hero.level)
        self.assertEqual(73, self.hero.health)
        self.assertEqual(15, self.hero.damage)

    def test_battle_result_is_defeat(self):
        self.hero.level = 1
        self.assertEqual("You lose", self.hero.battle(self.enemy_hero))
        self.assertEqual(81, self.enemy_hero.level)
        self.assertEqual(195, self.enemy_hero.health)
        self.assertEqual(17, self.enemy_hero.damage)

    def test_str_magic_method_returns_correct_string(self):
        self.assertEqual(f"Hero Link: 64 lvl\n"
                         f"Health: 80\n"
                         f"Damage: 10\n", self.hero.__str__())

if __name__ == "__main__":
    main()