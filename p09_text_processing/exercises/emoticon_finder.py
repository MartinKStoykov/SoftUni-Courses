text = "".join(input().split())
for letter in range(len(text)):
    if text[letter] == ":":
        print(text[letter] + text[letter+1])