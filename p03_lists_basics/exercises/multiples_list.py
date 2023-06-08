num1 = int(input())
num2 = int(input())
number_list = []
for num in range(num1, num2 * num1 +1):
    if num % num1 == 0:
        number_list.append(num)
print(number_list)