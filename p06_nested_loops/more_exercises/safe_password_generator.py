a = int(input())
b = int(input())
max_passwords = int(input())
passwords = 1
up_a = 35
up_b = 64
operation = True
while operation:
    for x1 in range(1, a+1):
        for x2 in range(1, b+1):
            print(f"{chr(up_a)}{chr(up_b)}{x1}{x2}{chr(up_b)}{chr(up_a)}", end="|")
            up_b += 1
            up_a += 1
            passwords += 1
            if up_b > 96:
                up_b = 64
            if up_a > 55:
                up_a = 35
            if (a == x1 and b == x2) or not passwords <= max_passwords:
                operation = False
                break
        if not operation:
            break
