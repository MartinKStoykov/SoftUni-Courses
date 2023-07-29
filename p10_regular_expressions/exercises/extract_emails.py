import re

text = input()
regex = r"\s([a-zA-Z0-9]+[.\-_]?[a-zA-Z0-9]+@[a-zA-Z]+[\-a-zA-Z]+\.[a-zA-Z]+[.a-zA-Z]+)\b"
emails_found = re.findall(regex, text)
print("\n".join(emails_found))