number = int(input())
while True:
    number += 1
    number_list = set(str(number))
    if len(number_list) == len(str(number)):
        print(number)
        break