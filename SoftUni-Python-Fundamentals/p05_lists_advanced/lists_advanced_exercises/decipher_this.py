secret_message = input().split()
def decipher(word):
    letters = []
    number = ""
    for char in word:
        if char.isdigit():
            number += char
        else:
            letters.append(char)
    letters[0], letters[-1] = letters[-1], letters[0]
    letters.insert(0, chr(int(number)))
    return "".join(letters)

for string in secret_message:
    print(decipher(string), end=" ")
