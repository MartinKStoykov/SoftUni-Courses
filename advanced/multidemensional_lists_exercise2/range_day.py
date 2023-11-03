gun_range = []
position = []
starting_targets = 0
for i in range(5):
    gun_range.append(input().split())
    starting_targets += gun_range[i].count("x")
    if "A" in gun_range[i]:
        position = [i, gun_range[i].index("A")]

command_num = int(input())
direction = {"right": [0, 1], "left": [0, -1], "up": [-1, 0], "down": [1, 0]}
targets_shot = []
for _ in range(command_num):
    command = input().split()

    new_r = position[0]
    new_c = position[1]
    if command[0] == "move":
        steps = int(command[2])
        new_r += direction[command[1]][0] * steps
        new_c += direction[command[1]][1] * steps
        if 0 <= new_r < 5 and 0 <= new_c < 5 and gun_range[new_r][new_c] == ".":
            gun_range[position[0]][position[1]] = "."
            position = [new_r, new_c]
            gun_range[new_r][new_c] = "A"
    elif command[0] == "shoot":
        while 0 <= new_r+direction[command[1]][0] < 5 and 0 <= new_c+direction[command[1]][1] < 5:
            new_r += direction[command[1]][0]
            new_c += direction[command[1]][1]
            if gun_range[new_r][new_c] == "x":
                targets_shot.append([new_r, new_c])
                gun_range[new_r][new_c] = "."
                break
        if starting_targets == len(targets_shot):
            break
if starting_targets == len(targets_shot):
    print(f"Training completed! All {starting_targets} targets hit.")
else:
    print(f"Training not completed! {starting_targets-len(targets_shot)} targets left.")
print(*targets_shot, sep="\n")
