starting_number = int(input())
new_number = int(input())

while True:
    current_number = int(input())
    new_number += current_number

    if new_number >= starting_number:
        print(new_number)
        break
