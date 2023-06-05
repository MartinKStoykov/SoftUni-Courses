string = input()
string_list = string.split(", ")
for num in range(len(string_list)):
    if string_list[num] == "0":
        string_list.remove(string_list[num])
        string_list.append("0")
string_list = list(map(int, string_list))
print((string_list))