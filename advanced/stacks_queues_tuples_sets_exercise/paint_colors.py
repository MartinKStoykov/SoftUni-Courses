from collections import deque
string = deque(input().split())
found_colors = []
while string:
    if len(string) == 1:
        if string[0] in ["red", "yellow", "blue", "orange", "purple", "green"]:
            found_colors.append(string[0])
        string.pop()
    else:
        if string[0] + string[-1] in ["red", "yellow", "blue", "orange", "purple", "green"]:
            found_colors.append(string[0] + string[-1])
        elif string[-1] + string[0] in ["red", "yellow", "blue", "orange", "purple", "green"]:
            found_colors.append(string[-1] + string[0])
        else:
            if len(string[0]) > 1:
                string.insert(len(string) // 2, string[0][:-1])
            if len(string[-1]) > 1:
                string.insert(len(string) // 2, string[-1][:-1])
        string.popleft(), string.pop()

final_list = []
for color in found_colors:
    if color in ["orange", "purple", "green"]:
        if color == "orange" and "red" in found_colors and "yellow" in found_colors:
            final_list.append(color)
        elif color == "purple" and "red" in found_colors and "blue" in found_colors:
            final_list.append(color)
        elif color == "green" and "blue" in found_colors and "yellow" in found_colors:
            final_list.append(color)
    else:
        final_list.append(color)
print(final_list)