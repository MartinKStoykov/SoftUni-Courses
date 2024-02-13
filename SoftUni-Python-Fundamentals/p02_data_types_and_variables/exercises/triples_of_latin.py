number = int(input())
for x1 in range(97, 97 + number):
    for x2 in range(97, 97 + number):
        for x3 in range(97, 97 + number):
            print(f"{chr(x1)}{chr(x2)}{chr(x3)}")