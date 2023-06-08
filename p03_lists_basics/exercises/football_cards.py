team_list = input().split()
players_a = []
players_b = []
count = 0
game_over = False
while len(team_list) > count:

    if team_list[count] not in players_a and "A" in team_list[count]:
        players_a.append(team_list[count])
    elif team_list[count] not in players_b and "B" in team_list[count]:
        players_b.append(team_list[count])
    count += 1
    if len(players_b) > 4 or len(players_a) > 4:
        print(f"Team A - {11 - len(players_a)}; Team B - {11 - len(players_b)}")
        print("Game was terminated")
        break
else:
    print(f"Team A - {11 - len(players_a)}; Team B - {11 - len(players_b)}")




