animals = []
animal = str(input())
animals_list = animal.split(", ")
reversed_list = animals_list.index("wolf")
sheeps = 0
for crit in iter(reversed(animals_list)):
    if crit == "wolf":
        if 0 == sheeps:
            print(f"Please go away and stop eating my sheep")
            break
        else:
            print(f"Oi! Sheep number {sheeps}! You are about to be eaten by a wolf!")
            break
    sheeps += 1