rows, columns = input().split(", ")
matrix = [[int(x) for x in input().split()] for x in range(int(rows))]
for j in range(int(columns)):
    print(sum([x[j] for x in matrix]))