matrix_count = int(input())
full_numbers = [[int(num) for num in input().split(", ")] for x in range(matrix_count)]
primary_nums = [[num for num in full_numbers][x][x] for x in range(matrix_count)]
secondary_nums = [[num for num in full_numbers][matrix_count-1-x][x] for x in range(matrix_count-1, -1, -1)]
print(f"Primary diagonal: {', '.join([str(x) for x in primary_nums])}. Sum: {sum(primary_nums)}")
print(f"Secondary diagonal: {', '.join([str(x) for x in secondary_nums])}. Sum: {sum(secondary_nums)}")