command = input()
player_pool = {}
while command != "Season end":
    if "->" in command:
        player, position, skills = command.split(" -> ")
        if player not in player_pool:
            player_pool[player] = {position: int(skills)}

        elif position not in player_pool[player]:
            player_pool[player][position] = int(skills)

        elif player_pool[player][position] < int(skills):
            player_pool[player][position] = int(skills)

    if " vs " in command:
        player1, player2 = command.split(" vs ")
        points1 = 0
        points2 = 0
        if player1 in player_pool and player2 in player_pool:
            for role in player_pool[player1]:
                if role in player_pool[player2]:
                    points1 += player_pool[player1][role]
                    points2 += player_pool[player2][role]

            if points1 > points2:
                del player_pool[player2]
            elif points2 > points1:
                del player_pool[player1]
    command = input()
points_ranking = {}
for key, value in player_pool.items():
    for key1, value1 in value.items():
        if key not in points_ranking:
            points_ranking[key] = 0
        points_ranking[key] += value1

for k1, v1 in sorted(points_ranking.items(), key=lambda kv: (-kv[1], kv[0])):
    print(f"{k1}: {v1} skill")
    for k2, v2 in sorted(player_pool[k1].items(), key=lambda kv: (-kv[1], kv[0])):
        print(f"- {k2} <::> {v2}")

