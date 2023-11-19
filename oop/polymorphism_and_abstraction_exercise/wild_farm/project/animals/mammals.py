from project.animals.animal import Mammal
from project.food import Meat, Vegetable, Fruit, Seed, Food

class Mouse(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Squeak"

    def feed(self, food: Food):
        if food.__class__ != Fruit and food.__class__ != Vegetable:
            return Mammal.cant_eat(self, food)
        self.weight += 0.10 * food.quantity
        self.food_eaten += food.quantity

class Dog(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Woof!"

    def feed(self, food: Food):
        if food.__class__ != Meat:
            return Mammal.cant_eat(self, food)
        self.weight += 0.40 * food.quantity
        self.food_eaten += food.quantity

class Cat(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "Meow"

    def feed(self, food: Food):
        if food.__class__ != Meat and food.__class__ != Vegetable:
            return Mammal.cant_eat(self, food)
        self.weight += 0.30 * food.quantity
        self.food_eaten += food.quantity

class Tiger(Mammal):
    def __init__(self, name: str, weight: float, living_region: str, food_eaten: int = 0):
        super().__init__(name, weight, living_region, food_eaten)

    def make_sound(self):
        return "ROAR!!!"

    def feed(self, food: Food):
        if food.__class__ != Meat:
            return Mammal.cant_eat(self, food)
        self.weight += 1.00 * food.quantity
        self.food_eaten += food.quantity
