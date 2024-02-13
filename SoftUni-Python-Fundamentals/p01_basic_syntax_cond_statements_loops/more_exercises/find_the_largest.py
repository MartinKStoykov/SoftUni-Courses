number = int(input())
largest_number = ""
for num in range(10, -1, -1):
    for digit in str(number):
        if int(digit) == (num):
            largest_number += f"{digit}"
print(largest_number)