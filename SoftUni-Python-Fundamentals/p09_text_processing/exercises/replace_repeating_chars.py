string = str(input())
last_letter = string[0]
for letter in string:
    if last_letter != letter:
        print(last_letter, end="")
    last_letter = letter
print(last_letter)