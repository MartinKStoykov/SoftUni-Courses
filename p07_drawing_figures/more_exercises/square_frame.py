number = int(input())

for row in range(1, number + 1):
    for col in range(1, number + 1):
        if col == 1 or col == number:
            if row == 1 or row == number:
                print("+", end=" ")
            else:
                print("|", end=" ")
        else:
            print("-", end=" ")
    print()