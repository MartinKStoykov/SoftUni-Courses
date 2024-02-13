from project.player import Player

class Team:
    def __init__(self, __name: str, __rating: int):
        self.__name = __name
        self.__rating = __rating
        self.__players: list[Player] = []

    def add_player(self, player: Player):
        if player in self.__players:
            return f"Player {player.name} has already joined"
        self.__players.append(player)
        return f"Player {player.name} joined team {self.__name}"

    def remove_player(self, player_name: str):
        for player in self.__players:
            if player.name == player_name:
                p = player
                self.__players.remove(player)
                return p

        return f"Player {player_name} not found"
