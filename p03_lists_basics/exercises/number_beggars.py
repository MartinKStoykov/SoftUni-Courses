integer_string = input().split(", ")
beggars = int(input())
int_list = []
current_sum = 0
sum_list = []

for num in integer_string:
    int_list.append(int(num))
beggar  = 0

while beggar < beggars:
    for turn in range(beggar, len(int_list), beggars):
        current_sum += int_list[turn]

    beggar += 1
    sum_list.append(current_sum)
    current_sum = 0
print(sum_list)
