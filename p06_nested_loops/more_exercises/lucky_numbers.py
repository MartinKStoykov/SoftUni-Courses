number = int(input())
last = number
if number > 9:
    last = 10
for num1 in range(1, last):
    for num2 in range(1, last):
        for num3 in range(1, last):
            for num4 in range(1, last):
                if (num1 + num2) == (num4 + num3) and (number % (num1 + num2) == 0):
                    print(f"{num1}{num2}{num3}{num4}", end=" ")
                else:
                    continue
