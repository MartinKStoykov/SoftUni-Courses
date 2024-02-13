string_list = input().split(" ")
remove_n = int(input())
integer_list = []

for num in string_list:
    integer_list.append(int(num))

integer_list.sort()

for num in range(remove_n):
    string_list.remove(str(integer_list[num]))

print(", ".join(string_list))