rows, columns = input().split(", ")
max_sum = 0
cords = []
matrix = [[int(x) for x in input().split(", ")] for x in range(int(rows))]
for i in range(int(rows)-1):
    for j in range(int(columns)-1):
        current_numbers = [matrix[i][j], matrix[i][j+1], matrix[i+1][j], matrix[i+1][j+1]]
        if matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1] > max_sum:
            max_sum = sum(current_numbers)
            cords = current_numbers
print(cords[0], cords[1])
print(cords[2], cords[3])
print(max_sum)