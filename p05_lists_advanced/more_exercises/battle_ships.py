rows = int(input())
all_fields = []
for row in range(rows):
    field = list(map(int, input().split()))
    all_fields.append(field)
attacked = input().split(" ")
ships_destroyed = 0
for row in attacked:
    attack_row = int(row[0])
    attack_col = int(row[2])
    if all_fields[attack_row][attack_col] > 0:
        all_fields[attack_row][attack_col] -= 1
        if all_fields[attack_row][attack_col] == 0:
            ships_destroyed += 1
print(ships_destroyed)
