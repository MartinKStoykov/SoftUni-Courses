rows, columns = input().split()
matrix = [[x for x in input().split()] for n in range(int(rows))]
while True:
    command = input().split()
    if len(command) == 1:
        break
    if command[0] == "swap" and all(x.isdigit() for x in command[1:]) and len(command) == 5:
        cords0, cords1, cords2, cords3 = int(command[0]), int(command[1]), int(command[2]), int(command[3])
        if 0 <= cords0 < int(rows) and 0 <= cords1 < int(columns) \
                and 0 <= cords2 < int(rows) and 0 <= cords3 < int(columns):
            matrix[cords0][cords1], matrix[cords2][cords3] = matrix[cords2][cords3], matrix[cords0][cords1]
            for i in range(int(rows)):
                print(*matrix[i])
        else:
            print("Invalid input!")
    else:
        print("Invalid input!")
