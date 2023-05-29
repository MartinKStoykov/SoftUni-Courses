starting_number = int(input())
added_number = 1
while True:
    print(added_number)
    added_number *= 2
    added_number += 1
    if added_number > starting_number:
        break
