string1, string2 = input().split()
total_sum = 0
longest_word = str(max(string1, string2, key=len))
for char in range(len(longest_word)):
    if char >= len(string2) or char >= len(string1):
        total_sum += ord(longest_word[char])
    else:
        total_sum += ord(string1[char]) * ord(string2[char])

print(total_sum)