import re

text = input()
regex = r"\b_([a-zA-Z0-9]+)\b"
found_variable_names = re.findall(regex, text)
print(",".join(found_variable_names))