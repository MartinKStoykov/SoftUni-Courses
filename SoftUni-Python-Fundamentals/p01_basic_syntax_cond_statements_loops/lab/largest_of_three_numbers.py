from sys import maxsize
max_number = -maxsize
for num in range(3):
    number = float(input())
    if number > max_number:
        max_number = number
print(int(max_number))