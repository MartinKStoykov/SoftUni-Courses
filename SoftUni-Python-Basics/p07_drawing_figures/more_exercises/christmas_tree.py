numbers = int(input())
for row in range(numbers + 1):
    for blank in range(numbers - row):
        print(" ", end="")
    for star in range(row):
        print(f"*", end="")
    print(f" | ", end="")
    for star in range(row):
        print(f"*", end="")
    for blank in range(numbers - row):
        print(" ", end="")
    print()