numbers_list = input().split()
absolute_value = []

for num in numbers_list:
    absolute_value.append(abs(float(num)))

print(absolute_value)