import re

text = input()
word = input()
regex = fr"\b{word}\b"
word_count = len(re.findall(regex, text, re.I))
print(word_count)