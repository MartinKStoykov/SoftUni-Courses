matrix = []
num_sum = 0
rows, columns = input().split(", ")
for i in range(int(rows)):
    current_row = [int(x) for x in input().split(", ")]
    matrix.append(current_row)
    num_sum += sum(current_row)
print(num_sum)
print(matrix)