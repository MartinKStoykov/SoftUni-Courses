numbers = int(input())

largest_number = 0
final_number = 0

for num in range(numbers):
    current_number = int(input())
    if current_number > largest_number:
        largest_number = current_number
    final_number += current_number
final_number -= largest_number
if final_number == largest_number:
    print("Yes")
    print(f"Sum = {final_number}")
else:
    diff = abs(largest_number - final_number)
    print("No")
    print(f"Diff = {diff}")