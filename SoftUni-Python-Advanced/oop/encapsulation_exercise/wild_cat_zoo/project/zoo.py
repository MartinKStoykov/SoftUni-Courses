from project.animal import Animal
from project.worker import Worker
class Zoo:
    def __init__(self, name: str, __budget: int, __animal_capacity: int, __workers_capacity: int):
        self.name = name
        self.__budget = __budget
        self.__animal_capacity = __animal_capacity
        self.__workers_capacity = __workers_capacity
        self.animals = []
        self.workers = []

    def add_animal(self, animal: Animal, price):
        if price <= self.__budget and self.__animal_capacity > len(self.animals):
            self.animals.append(animal)
            self.__budget -= price
            return f"{animal.name} the {animal.__class__.__name__} added to the zoo"

        elif price > self.__budget:
            return "Not enough budget"
        return "Not enough space for animal"

    def hire_worker(self, worker: Worker):
        if self.__workers_capacity > len(self.workers):
            self.workers.append(worker)
            return f"{worker.name} the {worker.__class__.__name__} hired successfully"
        return "Not enough space for worker"

    def fire_worker(self, worker_name):
        for worker in self.workers:
            if worker.name == worker_name:
                self.workers.remove(worker)
                return f"{worker_name} fired successfully"
        return f"There is no {worker_name} in the zoo"

    def pay_workers(self):
        salary_sum = sum([w.salary for w in self.workers])
        if self.__budget >= salary_sum:
            self.__budget -= salary_sum
            return f"You payed your workers. They are happy. Budget left: {self.__budget}"
        return "You have no budget to pay your workers. They are unhappy"

    def tend_animals(self):
        tending_sum = sum([a.money_for_care for a in self.animals])
        if self.__budget >= tending_sum:
            self.__budget -= tending_sum
            return f"You tended all the animals. They are happy. Budget left: {self.__budget}"
        return "You have no budget to tend the animals. They are unhappy."

    def profit(self, amount):
        self.__budget += amount

    def animals_status(self):
        animal_dict = {"Lion": [], "Tiger": [], "Cheetah": []}
        for animal in self.animals:
            animal_dict[animal.__class__.__name__].append(animal)
        result = f"You have {len(self.animals)} animals"
        result += (f"\n----- {len(animal_dict['Lion'])} Lions:\n" +
                   '\n'.join([repr(a) for a in self.animals if a.__class__.__name__ == "Lion"]))

        result += (f"\n----- {len(animal_dict['Tiger'])} Tigers:\n" +
                   '\n'.join([repr(a) for a in self.animals if a.__class__.__name__ == "Tiger"]))

        result += (f"\n----- {len(animal_dict['Cheetah'])} Cheetahs:\n" +
                   '\n'.join([repr(a) for a in self.animals if a.__class__.__name__ == "Cheetah"]))
        return result

    def workers_status(self):
        workers_dict = {"Keeper": [], "Caretaker": [], "Vet": []}
        for worker in self.workers:
            workers_dict[worker.__class__.__name__].append(worker)
        result = f"You have {len(self.workers)} workers"
        result += (f"\n----- {len(workers_dict['Keeper'])} Keepers:\n" +
                   '\n'.join([repr(a) for a in self.workers if a.__class__.__name__ == "Keeper"]))

        result += (f"\n----- {len(workers_dict['Caretaker'])} Caretakers:\n" +
                   '\n'.join([repr(a) for a in self.workers if a.__class__.__name__ == "Caretaker"]))

        result += (f"\n----- {len(workers_dict['Vet'])} Vets:\n" +
                   '\n'.join([repr(a) for a in self.workers if a.__class__.__name__ == "Vet"]))
        return result



