number_count = int(input())
number_list = []
filtered_list = []
for num in range(number_count):
    current_number = int(input())
    number_list.append(current_number)
command = input()
for num in range(len(number_list)):
    fits_category = (
        command == "even" and number_list[num] % 2 == 0 or
        command == "odd" and number_list[num] % 2 != 0 or
        command == "negative" and number_list[num] < 0 or
        command == "positive" and number_list[num] >= 0
        )
    if fits_category:
        filtered_list.append(number_list[num])
print(filtered_list)