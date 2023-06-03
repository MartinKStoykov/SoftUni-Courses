key = int(input())
numbers = int(input())
word = ""
for char in range(numbers):
    letter = (input())
    word += chr(ord(letter) + key)
print(word)