from sys import maxsize
rows, columns = input().split()
matrix = [[int(x) for x in input().split()] for n in range(int(rows))]
max_sum = -maxsize
max_matrix = []
for i in range(0, abs(int(rows)-2)):
    for j in range(0, abs(int(columns)-2)):
        curr_sum = [matrix[i][j:j+3], matrix[i+1][j:j+3], matrix[i+2][j:j+3]]
        if sum([x for lst in curr_sum for x in lst]) > max_sum:
            max_matrix = curr_sum
            max_sum = sum([x for lst in curr_sum for x in lst])

print("Sum =", sum([x for lst in max_matrix for x in lst]))
for item in max_matrix:
    print(*item)
