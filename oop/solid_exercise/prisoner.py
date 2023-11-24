import copy

class Person:
    def __init__(self, position):
        self.position = position
        self.is_free = None


class FreePerson(Person):

    def __init__(self, position):
        super().__init__(position)
        self.is_free = True

    def walk_north(self, dist):
        self.position[1] += dist

    def walk_east(self, dist):
        self.position[0] += dist


class Prisoner(Person):
    PRISON_LOCATION = (3, 3)

    def __init__(self):
        super(Prisoner, self).__init__(copy.copy(self.PRISON_LOCATION))
        self.is_free = False



