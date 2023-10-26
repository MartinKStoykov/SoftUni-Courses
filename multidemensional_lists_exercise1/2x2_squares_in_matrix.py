rows, columns = input().split()
matrix = [[x for x in input().split()] for n in range(int(rows))]
identical_squares = 0
for i in range(int(rows)-1):
    for j in range(int(columns)-1):
        if matrix[i][j] == matrix[i][j+1] == matrix[i+1][j] == matrix[i+1][j+1]:
            identical_squares += 1
print(identical_squares)