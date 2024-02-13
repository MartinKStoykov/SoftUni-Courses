from class_and_static_methods_exercise.document_managementt.project import DVD

class Customer:
    def __init__(self, name: str, age:int, id: int):
        self.name= name
        self.age= age
        self.id = id
        self.rented_dvds: list[DVD] = []

    def __repr__(self):
        return (f"{self.id}: {self.name} of age {self.age}"
                f" has {len(self.rented_dvds)} rented DVD's"
                f" ({', '.join([dvd.name for dvd in self.rented_dvds])})")
