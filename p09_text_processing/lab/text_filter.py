banned_words = input().split(", ")
text = str(input())

for word in banned_words:
    while word in text:
        text = text.replace(word, "*" * len(word))

print(text)