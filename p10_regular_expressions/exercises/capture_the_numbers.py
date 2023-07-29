import re
found_numbers = []
while True:
    text = input()
    if not text :
        break
    regex = r"\d+"
    found_numbers.extend(re.findall(regex, text))

print(" ".join(found_numbers))