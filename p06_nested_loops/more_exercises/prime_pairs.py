first_pair = int(input())
second_pair = int(input())
first_diff = int(input())
second_diff = int(input())
prime1 = False
prime2 = False
for x1 in range(first_pair, first_pair + first_diff +1):
    for x2 in range(second_pair, second_pair + second_diff +1):
        for num1 in range(2, x1):
            if x1 % num1 == 0:
                prime1 = True
                break
        for num2 in range(2, x2):
            if x2 % num2 == 0:
                prime2 = True
                break
        if not prime1 and not prime2:
            print(f"{x1}{x2}")
        prime1 = False
        prime2 = False

