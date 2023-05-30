decorations_to_buy = int(input())
days_to_christmas = int(input())
cost = 0
total_spirit = 0
for day in range(1, days_to_christmas+1):
    if day % 11 == 0:
        decorations_to_buy += 2
    if day % 2 == 0:
        cost += decorations_to_buy * 2
        total_spirit += 5
    if day % 3 == 0:
        cost += decorations_to_buy * 8
        total_spirit += 13
    if day % 5 == 0:
        cost += decorations_to_buy * 15
        total_spirit += 17
        if day % 3 == 0:
            total_spirit += 30
    if day % 10 == 0:
        total_spirit -= 20
        cost += 23
        if days_to_christmas == day:
            total_spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {total_spirit}")