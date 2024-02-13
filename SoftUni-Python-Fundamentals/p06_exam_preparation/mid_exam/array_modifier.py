array_list = list(map(int, input().split()))
command = input().split()
while command[0] != "end":
    action = command[0]
    if action == "decrease":
        for num in range(len(array_list)):
            array_list[num] -= 1
    else:
        index1 = int(command[1])
        index2 = int(command[2])
        if action == "swap":
            array_list[index1], array_list[index2] = array_list[index2], array_list[index1]

        elif action == "multiply":
            array_list[index1] = array_list[index1] * array_list[index2]
    command = input().split()
string_list = [str(num) for num in array_list]
print(", ".join(string_list))