from math import ceil
numbers = int(input())
double = numbers * 2
print("*" * double, end="")
print(f" " * numbers, end="")
print("*" * double)
for inner in range(1, numbers - 1):
    if inner == ceil((numbers - 2) / 2):
        for row in range(1, numbers * 5 + 1):
            if row == 1 or row == numbers * 2 or row == (numbers * 3) + 1 or row == numbers * 5:
                print(f"*", end="")
            elif 1 < row < numbers * 2 or numbers * 3 + 1 < row < numbers * 5:
                print(f"/", end="")
            else:
                print(f"|", end="")
        print()
    else:
        for row in range(1, numbers * 5 + 1):
            if row == 1 or row == numbers * 2 or row == (numbers * 3) + 1 or row == numbers * 5:
                print(f"*", end="")
            elif 1 < row < numbers * 2 or numbers * 3 + 1 < row < numbers * 5:
                print(f"/", end="")
            else:
                print(f" ", end="")
        print()


print("*" * double, end="")
print(f" " * numbers, end="")
print("*" * double)