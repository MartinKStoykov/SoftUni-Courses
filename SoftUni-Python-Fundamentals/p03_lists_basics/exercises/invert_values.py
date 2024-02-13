numbers_string = input().split()
numbers_list = []
for num in range(len(numbers_string)):
    numbers_list.append(-int(numbers_string[num]))
print(numbers_list)