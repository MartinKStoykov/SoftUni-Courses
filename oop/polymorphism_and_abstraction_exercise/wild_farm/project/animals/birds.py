from project.animals.animal import Bird
from project.food import Meat, Vegetable, Fruit, Seed, Food

class Owl(Bird):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Hoot Hoot"

    def feed(self, food: Food):
        if food.__class__ != Meat:
            return Bird.cant_eat(self, food)
        self.weight += 0.25 * food.quantity
        self.food_eaten += food.quantity


class Hen(Bird):
    def __init__(self, name: str, weight: float, wing_size: float, food_eaten: int = 0):
        super().__init__(name, weight, wing_size, food_eaten)

    def make_sound(self):
        return "Cluck"

    def feed(self, food: Food):
        self.weight += 0.35 * food.quantity
        self.food_eaten += food.quantity
