elements = input().split()
odd_occurrences = {}

for element in elements:

    if element.lower() not in odd_occurrences:
        odd_occurrences[element.lower()] = 0
    odd_occurrences[element.lower()] += 1

for key, value in odd_occurrences.items():
    if value % 2 != 0:
        print(key, end=" ")