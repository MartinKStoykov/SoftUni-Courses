numbers = list(map(int, input().split(", ")))
group = 10

while max(numbers) + 10 > group:
    group_list = [number for number in numbers if (group - 10) < number <= group]
    print(f"Group of {group}'s:", group_list)
    group += 10
