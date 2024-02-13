numbers = int(input()) * 2

left_sum = 0
right_sum = 0
diff = 0
for num in range(numbers):
    number = int(input())
    if num < (numbers / 2):
        left_sum += number
    elif num >= (numbers / 2):
        right_sum += number
    diff = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {diff}")

