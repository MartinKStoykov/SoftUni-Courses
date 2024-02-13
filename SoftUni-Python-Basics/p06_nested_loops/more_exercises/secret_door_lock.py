first_max = int(input())
second_max = int(input())
third_max = int(input())
for first in range(1, first_max+1):
    for second in range(1, second_max+1):
        for third in range(1, third_max+1):
            if first % 2 == 0 and third % 2 == 0 and 2 <= second <= 7 and second != 4 and second != 6:
                print(f"{first} {second} {third}")