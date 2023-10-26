matrix_count = int(input())
full_numbers = [[int(num) for num in input().split()] for x in range(matrix_count)]
primary_nums = sum([num for num in full_numbers][x][x] for x in range(matrix_count))
secondary_nums = sum([num for num in full_numbers][matrix_count-1-x][x] for x in range(matrix_count-1, -1, -1))
print(abs(primary_nums - secondary_nums))