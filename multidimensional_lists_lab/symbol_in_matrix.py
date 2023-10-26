matrix_size = int(input())
matrix = [[x for x in input()] for x in range(matrix_size)]
searched_char = input()
for j in matrix:
    if searched_char in j:
        print(f"({matrix.index(j)}, {j.index(searched_char)})")
        break
else:
    print(f"{searched_char} does not occur in the matrix")