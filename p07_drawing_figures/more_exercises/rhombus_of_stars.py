numbers = int(input())
blank_space = " "
star = "*"
for row in range(1, numbers):
    for blank in range(numbers - row):
        print(" ", end="")
    for star in range(row):
        print("*", end=" ")
    print()
print(f"* " * numbers)
for row in range(numbers-1, 0, -1):
    for blank in range(numbers - row):
        print(" ", end="")
    for star in range(row):
        print("*", end=" ")
    print()