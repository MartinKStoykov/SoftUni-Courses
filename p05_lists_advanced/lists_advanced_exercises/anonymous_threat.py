def merging(strings, start, end):
    if start < 0:
        start = 0
    strings[start:end+1] = ["".join(strings[start:end+1])]
    return strings
def dividing(string, index, divisions):
    to_divide = string[index]
    length = len(to_divide) // divisions
    is_zero = False
    if length == 0:
        length = 1
        is_zero = True
    first_half = string[:index]
    divided_string = [to_divide[i:i + length] for i in range(0, len(to_divide), length)]
    if len(divided_string) != divisions or is_zero:
        divided_string[-2:] = ["".join(divided_string[-2:])]
    second_half = string[index+1:]
    final_list = first_half + divided_string + second_half

    return final_list
string_list = input().split()
command = input().split()

while command[0] != "3:1":
    action = command[0]
    first_index = int(command[1])
    second_index = int(command[2])
    if action == "merge":
        string_list = merging(string_list, first_index, second_index)
    elif action == "divide":
        string_list = dividing(string_list, first_index, second_index)
    if "" in string_list:
        string_list.remove("")
    command = input().split()
print(*string_list)