from math import ceil, floor

numbers = int(input())
if numbers % 2 == 0:
    stars = 2
    for row in range(1, ceil(numbers / 2) + 1):
        for col in range(1):
            print("-" * ceil((numbers - stars) / 2), end="")
            print("*" * stars,  end="")
            print("-" * ceil((numbers - stars) / 2), end="")
        stars += 2
        print()
else:
    stars = 1
    for row in range(1, ceil(numbers / 2) + 1):
        for col in range(1):
            print("-" * ceil((numbers - stars) / 2), end="")
            print("*" * stars,  end="")
            print("-" * ceil((numbers - stars) / 2), end="")
        stars += 2
        print()
for row in range(1, floor(numbers / 2) + 1):
    for col in range(1):
        print("|", end="")
        print("*" * (numbers - 2), end="")
        print("|", end="")
    print()