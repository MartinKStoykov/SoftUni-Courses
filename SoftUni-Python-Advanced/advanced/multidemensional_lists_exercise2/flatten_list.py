initial_lists = input().split("|")
print(*[num for lst in reversed(initial_lists) for num in lst.split()])