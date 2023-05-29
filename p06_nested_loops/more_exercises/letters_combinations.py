first_letter = str(input())
second_letter = str(input())
third_letter = str(input())
bad_letter = ord(third_letter)
combos = 0

for x1 in range(ord(first_letter), ord(second_letter) + 1):
    for x2 in range(ord(first_letter), ord(second_letter) + 1):
        for x3 in range(ord(first_letter), ord(second_letter) + 1):
            if x1 == bad_letter or x2 == bad_letter or x3 == bad_letter:
                continue
            else:
                combos += 1
                print(f"{chr(x1)}{chr(x2)}{chr(x3)}", end=" ")

print(combos)