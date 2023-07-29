import re

phone_numbers = input()
regex = r"\+359-2-\d{3}-\d{4}\b|\+359 2 \d{3} \d{4}\b"

phones = re.findall(regex, phone_numbers)
print(", ".join(phones))