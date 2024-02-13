from math import ceil, floor

numbers = int(input())
if numbers % 2 == 0:
    middle = 0
else:
    middle = 1
if numbers == 3:
    print("-*-")
if numbers == 1:
    print("*" * numbers)
for row in range(1, floor(numbers / 2)):
    if middle == 1:
        print("-" * floor(numbers / 2), end="")
        print("*", end="")
        print("-" * floor(numbers / 2), end="")
        print()
    for col in range(1):
        print("-" * floor((numbers - 2 - middle) / 2), end="")
        print("*",  end="")
        print("-" * middle, end="")
        print("*", end="")
        print("-" * floor((numbers - 2 - middle) / 2), end="")
        middle += 2
    print()
for row in range(floor(numbers / 2) + 1, 1, - 1):
    for col in range(1):
        print("-" * floor((numbers - 2 - middle) / 2), end="")
        print("*", end="")
        print("-" * middle, end="")
        print("*", end="")
        print("-" * floor((numbers - 2 - middle) / 2), end="")
        middle -= 2
    print()
if middle == -1:
    print("-" * floor(numbers / 2), end="")
    print("*", end="")
    print("-" * floor(numbers / 2), end="")
