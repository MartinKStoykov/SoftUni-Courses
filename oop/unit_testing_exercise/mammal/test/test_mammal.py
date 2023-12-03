from unittest import TestCase, main

from project.mammal import Mammal


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Chris P. Bacon", "pig", "oink")

    def test_initialization(self):
        self.assertEqual("Chris P. Bacon", self.mammal.name)
        self.assertEqual("pig", self.mammal.type)
        self.assertEqual("oink", self.mammal.sound)

    def test_make_sound_returns_correct_string(self):
        self.assertEqual("Chris P. Bacon makes oink", self.mammal.make_sound())

    def test_get_kingdom_returns_correct_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info_returns_correct_string(self):
        self.assertEqual("Chris P. Bacon is of type pig", self.mammal.info())

if __name__ == "__main__":
    main()