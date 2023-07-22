character1 = ord(str(input()))
character2 = ord(str(input()))
string = str(input())
total_sum = 0
for char in string:
    if character1 < ord(char) < character2:
        total_sum += ord(char)

print(total_sum)