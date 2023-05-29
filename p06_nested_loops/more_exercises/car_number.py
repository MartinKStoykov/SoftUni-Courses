start = int(input())
end = int(input())
for num1 in range(start, end+1):
    for num2 in range(start, end+1):
        for num3 in range(start, end+1):
            for num4 in range(start, end+1):
                if num1 % 2 == 0:
                    if (num2 + num3) % 2 == 0 and num1 > num4 and num4 % 2 == 1:
                            print(f"{num1}{num2}{num3}{num4}", end=" ")
                elif num1 % 2 == 1:
                    if (num2 + num3) % 2 == 0 and num1 > num4 and num4 % 2 == 0:
                            print(f"{num1}{num2}{num3}{num4}", end=" ")
                else:
                    if (num2 + num3) % 2 == 0 and num1 > num4 and num4 % 2 == 0:
                            print(f"{num1}{num2}{num3}{num4}", end=" ")
