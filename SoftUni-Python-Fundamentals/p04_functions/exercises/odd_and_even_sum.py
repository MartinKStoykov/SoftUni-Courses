def sum_even_odd(numbers):
    odd_sum = 0
    even_sum = 0
    for num in range(0, len(numbers)):
        if int(numbers[num]) % 2 == 0:
            even_sum += int(numbers[num])
        elif int(numbers[num]) % 2 == 1:
            odd_sum += int(numbers[num])
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


number = str(input())
print(sum_even_odd(number))