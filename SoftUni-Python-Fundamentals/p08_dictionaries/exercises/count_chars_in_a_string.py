string = "".join(input().split())
char_count = {}
for x in range(len(string)):
    char = string[x]
    if char not in char_count:
        char_count[char] = 0
    char_count[char] += 1

for key, value in char_count.items():
    print(f"{key} -> {value}")