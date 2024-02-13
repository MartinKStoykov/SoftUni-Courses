from abc import ABC, abstractmethod

class Animal(ABC):
    def __init__(self, species):
        self.species = species

    @staticmethod
    @abstractmethod
    def make_sound():
        pass

class Cat(Animal):

    @staticmethod
    def make_sound():
        return "meow"

class Dog(Animal):
    @staticmethod
    def make_sound():
        return "woof-woof"

class Chicken(Animal):
    @staticmethod
    def make_sound():
        return "cluck"

def animal_sound(animals):
    for animal in animals:
        print(animal.make_sound())