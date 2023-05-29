num1 = int(input())
num2 = int(input())
for x1 in range(1, num1):
    for x2 in range(1, num1):
        for l1 in range(97, 97 + num2):
            for l2 in range(97, 97 + num2):
                for x3 in range(1, num1+1):
                    if x3 > x1 and x3 > x2:
                        print(f"{x1}{x2}{chr(l1)}{chr(l2)}{x3}", end=" ")
