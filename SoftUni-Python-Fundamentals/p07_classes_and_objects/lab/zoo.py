class Zoo:
    __animals = 0
    def __init__(self, name):
        self.name = name
        self.mammals = []
        self.fishes = []
        self.birds = []
    def add_animal(self, species, name):
        if species == "mammal":
            self.mammals.append(name)
        elif species == "fish":
            self.fishes.append(name)
        elif species == "bird":
            self.birds.append(name)
        Zoo.__animals += 1
    def get_info(self, species):
        message = ""
        if species == "mammal":
            message = f"Mammals in {self.name}: {', '.join(self.mammals)}\n"
        elif species == "fish":
            message = f"Fishes in {self.name}: {', '.join(self.fishes)}\n"
        elif species == "bird":
            message = f"Birds in {self.name}: {', '.join(self.birds)}\n"
        message += f"Total animals: {Zoo.__animals}"
        return message

zoo_name = str(input())
zoo = Zoo(zoo_name)
animal_count = int(input())
for num in range(animal_count):
    animal = input().split()
    zoo.add_animal(animal[0], animal[1])
species_check = str(input())
print(zoo.get_info(species_check))