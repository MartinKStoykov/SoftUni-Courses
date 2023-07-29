import re

names = input()
regex = "\\b[A-Z][a-z]+ [A-Z][a-z]+\\b"
found_names = re.findall(regex, names)

for name in found_names:
    print(name, end=" ")