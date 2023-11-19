from class_and_static_methods_exercise.document_managementt.project import Room

class Hotel:
    def __init__(self, name: str):
        self.name = name
        self.rooms = []
        self.guests = 0

    @classmethod
    def from_stars(cls, star_count: int):
        return cls(f"{star_count} stars Hotel")

    def add_room(self, room: Room):
        self.rooms.append(room)

    def take_room(self, room_number, people):
        for r in self.rooms:
            if r.number == room_number:
                r.take_room(people)
                self.guests += people

    def free_room(self, room_number):
        for r in self.rooms:
            if r.number == room_number:
                self.guests -= r.guests
                return r.free_room()


    def status(self):
        return (f"Hotel {self.name} has {self.guests} total guests\n"
                f"Free rooms: {', '.join([str(r.number) for r in self.rooms if not r.is_taken])}\n"
                f"Taken rooms: {', '.join([str(r.number) for r in self.rooms if r.is_taken])}")


