from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit

class Mouse(Mammal):
    WEIGHT_GAIN = 0.10

    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Squeak"

    def edible_food(self):
        return [Vegetable, Fruit]


class Dog(Mammal):
    WEIGHT_GAIN = 0.40

    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Woof!"

    def edible_food(self):
        return [Meat]

class Cat(Mammal):
    WEIGHT_GAIN = 0.30

    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Meow"

    def edible_food(self):
        return [Meat, Vegetable]

class Tiger(Mammal):
    WEIGHT_GAIN = 1.00

    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "ROAR!!!"

    def edible_food(self):
        return [Meat]