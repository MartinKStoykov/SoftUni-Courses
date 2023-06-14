names = input().split(", ")
sorted_names = [name for name in sorted(names, key=lambda name: (-len(name), name))]
print(sorted_names)