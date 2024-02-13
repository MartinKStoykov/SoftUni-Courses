numbers = input().split()
total_value = 0
while numbers:
    numbers = [int(num) for num in numbers]
    index = int(input())
    current_value = 0
    if index < 0:
        current_value = numbers[0]
        numbers[0] = numbers[-1]
    elif index > len(numbers)-1:
        current_value = numbers[-1]
        numbers[-1] = numbers[0]
    else:
        current_value = numbers.pop(index)

    for num in range(len(numbers)):
        if numbers[num] <= current_value:
            numbers[num] += current_value
        elif numbers[num] > current_value:
            numbers[num] -= current_value
    total_value += current_value
print(total_value)