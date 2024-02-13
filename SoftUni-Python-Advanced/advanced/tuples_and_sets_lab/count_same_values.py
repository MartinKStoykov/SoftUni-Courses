numbers = input().split()
occurrences = {}

for num in numbers:
    occurrences[num] = numbers.count(num)

for numb, count in occurrences.items():
    print(f"{float(numb):.1f} - {count} times")