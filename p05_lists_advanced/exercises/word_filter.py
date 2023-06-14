text = input().split()
filtered_list = [word for word in text if len(word) % 2 == 0]
print(*filtered_list, sep= "\n")