text = input()
occurrences = {}
for char in text:
    occurrences[char] = text.count(char)

for char, count in sorted(occurrences.items()):
    print(f"{char}: {count} time/s")