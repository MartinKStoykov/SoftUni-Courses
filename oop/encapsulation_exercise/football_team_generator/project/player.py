class Player:
    __players = []
    def __init__(self, __name: str, __sprint: int, __dribble: int, __passing: int, __shooting: int):
        self.__name = __name
        self.__sprint = __sprint
        self.__dribble = __dribble
        self.__passing = __passing
        self.__shooting = __shooting

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    def __str__(self):
        return (f"Player: {self.__name}\nSprint: {self.__sprint}\nDribble:"
                f" {self.__dribble}\nPassing: {self.__passing}\nShooting: {self.__shooting}")
