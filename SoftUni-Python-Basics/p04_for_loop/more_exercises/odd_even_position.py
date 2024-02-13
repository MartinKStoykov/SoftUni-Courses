from sys import maxsize
numbers = int(input())
odd_sum = 0
even_sum = 0
min_number_even = maxsize
max_number_even = -maxsize
min_number_odd = maxsize
max_number_odd = -maxsize
digit = 1
for num in range(numbers):
    current_number = float(input())
    if digit % 2 == 0:
        even_sum += current_number
        if current_number < min_number_even:
            min_number_even = current_number
        if current_number > max_number_even:
            max_number_even = current_number
    elif digit % 2 == 1:
        odd_sum += current_number
        if current_number < min_number_odd:
            min_number_odd = current_number
        if current_number > max_number_odd:
            max_number_odd = current_number
    digit += 1
print(f"OddSum={odd_sum:.2f},")
if numbers == 0:
    print(f"OddMin=No,")
    print(f"OddMax=No,")
else:
    print(f"OddMin={min_number_odd:.2f},")
    print(f"OddMax={max_number_odd:.2f},")
print(f"EvenSum={even_sum:.2f},")
if numbers <= 1:
    print(f"EvenMin=No,")
    print(f"EvenMax=No")
else:
    print(f"EvenMin={min_number_even:.2f},")
    print(f"EvenMax={max_number_even:.2f}")