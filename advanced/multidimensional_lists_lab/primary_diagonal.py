matrix_size = int(input())
num_sum = 0
for row in range(matrix_size):
    num_sum += int(input().split()[row])

print(num_sum)