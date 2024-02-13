from sys import maxsize
string_list = str(input()).split()
command = input().split()
int_list = []
for num in string_list:
    int_list.append(int(num))

while command[0] != "end":
    even_list = [even for even in int_list if even % 2 == 0]
    odd_list = [odd for odd in int_list if odd % 2 != 0]
    max_number = -maxsize
    min_num = maxsize
    num_found = False
    count = 0
    index_value = 0
    if command[0] == "exchange":
        if int(command[1]) >= len(int_list) or int(command[1]) < 0:
            print("Invalid index")
        else:
            for num in range(0, int(command[1])+1):
                int_list.append(int_list[num])
            for num in range(0, int(command[1])+1):
                int_list.remove(int_list[0])
    elif command[0] == "max":
        if command[1] == "even":
            for index, num in enumerate(int_list):
                if max_number <= num and num % 2 == 0:
                    max_number = num
                    num_found = True
                    index_value = index
        elif command[1] == "odd":
            for index, num in enumerate(int_list):
                if max_number <= num and num % 2 != 0:
                    max_number = num
                    num_found = True
                    index_value = index
        if not num_found:
            print("No matches")
        else:
            print(index_value)
    elif command[0] == "min":
        if command[1] == "even":
            for index, num in enumerate(int_list):
                if num <= min_num and num % 2 == 0:
                    min_num = num
                    num_found = True
                    index_value = index
        elif command[1] == "odd":
            for index, num in enumerate(int_list):
                if num <= min_num and num % 2 != 0:
                    min_num = num
                    num_found = True
                    index_value = index
        if not num_found:
            print("No matches")
        else:
            print(index_value)
    elif command[0] == "first":
        count = int(command[1])
        if count > len(int_list):
            print("Invalid count")
        else:
            if command[2] == "odd":
                print(odd_list[:count])
            elif command[2] == "even":
                print(even_list[:count])
    elif command[0] == "last":
        count = int(command[1])
        if count > len(int_list):
            print("Invalid count")
        else:
            if command[2] == "odd":
                print(odd_list[-count:])
            elif command[2] == "even":
                print(even_list[-count:])
    command = input().split()
print(int_list)
