numbers = sorted(list(map(int, input().split())), reverse=True)
average = sum(numbers) / len(numbers)
greater_than_average = [num for num in numbers if num > average]
if not greater_than_average:
    print("No")
else:
    print(*greater_than_average[:5])