numbers = int(input())
even_sum = 0
odd_sum = 0
for num in range(numbers):
    number = int(input())
    if num % 2 == 0:
        even_sum += number
    else:
        odd_sum += number

if even_sum == odd_sum:
    print("Yes")
    print(f"Sum = {odd_sum}")

else:
    diff = abs(odd_sum - even_sum)
    print("No")
    print(f"Diff = {diff}")
