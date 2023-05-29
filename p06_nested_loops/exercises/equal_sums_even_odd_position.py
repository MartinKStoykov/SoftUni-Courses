num1 = int(input())
num2 = int(input())

for number in range(num1, num2 + 1):
    odd_sum = 0
    even_sum = 0
    number_to_string = str(number)
    for i in range(len(number_to_string)):
        if i % 2 == 0:
            even_sum += int(number_to_string[i])
        else:
            odd_sum += int(number_to_string[i])
    if odd_sum == even_sum:
        print(number, end=" ")
