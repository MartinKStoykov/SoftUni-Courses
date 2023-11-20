from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed

class Owl(Bird):
    WEIGHT_GAIN = 0.25

    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Hoot Hoot"

    def edible_food(self):
        return [Meat]

class Hen(Bird):
    WEIGHT_GAIN = 0.35

    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Cluck"

    def edible_food(self):
        return [Meat, Vegetable, Fruit, Seed]

