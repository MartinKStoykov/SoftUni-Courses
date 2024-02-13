strings = input().split()
processed_numbers = 0
for string in strings:
    current_num = 0
    if string[0].isupper():
        current_num += int(string[1:-1]) / (ord(string[0]) - 64)

    elif string[0].islower():
        current_num += int(string[1:-1]) * (ord(string[0]) - 96)

    if string[-1].isupper():
        current_num -= ord(string[-1]) -64

    elif string[-1].islower():
        current_num += ord(string[-1]) -96

    processed_numbers += current_num

print(f"{processed_numbers:.2f}")