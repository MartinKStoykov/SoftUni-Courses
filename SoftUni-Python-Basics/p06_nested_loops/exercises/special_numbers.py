n = int(input())
for num in range(1111, 9999):
    number_is_false = False
    number_to_str = str(num)
    for i in range(len(number_to_str)):
        current_number = int(number_to_str[i])
        if current_number == 0 or n % current_number != 0:
            number_is_false = True
    if not number_is_false:
        print(num, end= " ")