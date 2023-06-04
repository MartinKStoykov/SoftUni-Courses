number_count = int(input())
positive_list = []
negative_list = []
for num in range(number_count):
    current_number = int(input())
    if current_number >= 0:
        positive_list.append(current_number)
    else:
        negative_list.append(current_number)
print(f"{positive_list} \n{negative_list}")
print(f"Count of positives: {len(positive_list)} \nSum of negatives: {sum(negative_list)}")