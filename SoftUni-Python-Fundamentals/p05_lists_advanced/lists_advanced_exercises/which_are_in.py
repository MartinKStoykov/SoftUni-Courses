first_string = input().split(", ")
second_string = input().split(", ")
common_strings = []
for string in first_string:
    for sub_string in second_string:
        if string in sub_string:
            common_strings.append(string)
            break
print(common_strings)