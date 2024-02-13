starting_interval = int(input())
ending_interval = int(input())
magic_number = int(input())
combination_number = 0
combination_found = False
for i1 in range(starting_interval, ending_interval + 1):
    for i2 in range(starting_interval, ending_interval + 1):
        combination_number += 1
        if i1 + i2 == magic_number:
            print(f"Combination N:{combination_number} ({i1} + {i2} = {magic_number})")
            combination_found = True
            break
    if combination_found:
        break

if not combination_found:
    print(f"{combination_number} combinations - neither equals {magic_number}")
