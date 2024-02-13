from sys import maxsize
field_size = int(input())
field = []
bunny = []
for row in range(field_size):
    field.append(input().split())
    if "B" in field[row]:
        bunny = [row, field[row].index("B")]

directions = {"right": [0, 1], "down": [1, 0], "left": [0, -1], "up": [-1, 0]}
total_max = -maxsize
final_indices = []
final_direction = ""
for key, d in directions.items():
    curr_location = [bunny[0], bunny[1]]
    curr_max = 0
    curr_indices = []
    while 0 <= curr_location[0] + d[0] < field_size and 0 <= curr_location[1] + d[1] < field_size:
        curr_location[0] += d[0]
        curr_location[1] += d[1]
        if field[curr_location[0]][curr_location[1]] == "X":
            break
        curr_max += int(field[curr_location[0]][curr_location[1]])
        curr_indices.append([curr_location[0], curr_location[1]])
    if curr_max > total_max:
        total_max = curr_max
        final_indices = curr_indices
        final_direction = key

print(final_direction)
for index in final_indices:
    print(index)
print(total_max)