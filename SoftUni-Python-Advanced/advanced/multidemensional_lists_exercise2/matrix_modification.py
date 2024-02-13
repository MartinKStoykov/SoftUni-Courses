rows = int(input())
matrix = []
for i in range(rows):
    matrix.append([int(num) for num in input().split()])

while True:
    command = input().split()
    if len(command) == 1:
        break
    action = command[0]
    row = int(command[1])
    col = int(command[2])
    value = int(command[3])
    if action == "Add" and 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        matrix[row][col] += value
    elif action == "Subtract" and 0 <= row < len(matrix) and 0 <= col < len(matrix[row]):
        matrix[row][col] -= value
    else:
        print("Invalid coordinates")

for row in matrix:
    print(*row)