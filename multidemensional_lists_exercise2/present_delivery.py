presents = int(input())
matrix_size = int(input())
neighborhood = []
santa = []
presents_given = 0
nice_kids = 0
for i in range(matrix_size):
    neighborhood.append(input().split())
    for j in range(matrix_size):
        if neighborhood[i][j] == "S":
            santa = [i, j]
        elif neighborhood[i][j] == "V":
            nice_kids += 1

directions = {"left": [0, -1], "right": [0, 1], "up": [-1, 0], "down": [1, 0]}
while presents and nice_kids != presents_given:
    command = input()
    if command == "Christmas morning":
        break
    new_r = santa[0]+directions[command][0]
    new_c = santa[1]+directions[command][1]
    if 0 <= new_r < matrix_size and 0 <= new_c < matrix_size:
        neighborhood[santa[0]][santa[1]] = "-"
        santa = [new_r, new_c]
        if neighborhood[new_r][new_c] == "V":
            presents_given += 1
            presents -= 1
        elif neighborhood[new_r][new_c] == "C":
            for values in directions.values():
                cookie_r = new_r + values[0]
                cookie_c = new_c + values[1]
                if 0 <= cookie_r < matrix_size and 0 <= cookie_c < matrix_size and presents > 0:
                    if neighborhood[cookie_r][cookie_c] != "-":

                        if neighborhood[cookie_r][cookie_c] == "V":
                            presents_given += 1
                        presents -= 1
                        neighborhood[cookie_r][cookie_c] = "-"

        neighborhood[new_r][new_c] = "S"
if presents == 0 and presents_given < nice_kids:
    print("Santa ran out of presents!")
[print(*r) for r in neighborhood]
if presents_given == nice_kids:
    print(f"Good job, Santa! {nice_kids} happy nice kid/s.")
else:
    print(f"No presents for {nice_kids-presents_given} nice kid/s.")