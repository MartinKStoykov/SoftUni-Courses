lines = int(input())
sum = 0
for line in range(lines):
    char = str(input())
    sum += ord(char)
print(f"The sum equals: {sum}")