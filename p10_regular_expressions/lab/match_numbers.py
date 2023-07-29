import re

numbers_list = input()
regex = r'(^|(?<=\s))-?([0]|[1-9][0-9]*)(\.\d+)?($|(?=\s))'
valid_numbers = re.finditer(regex, numbers_list)
for num in valid_numbers:
    print(num.group(), end=" ")