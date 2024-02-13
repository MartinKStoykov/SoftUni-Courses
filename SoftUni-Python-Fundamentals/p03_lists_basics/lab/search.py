number_count = int(input())
searched_word = str(input())
normal_list = []
filtered_list = []
for num in range(number_count):
    current_string = str(input())
    normal_list.append(current_string)
    if searched_word in current_string:
        filtered_list.append(current_string)
print(normal_list)
print(filtered_list)