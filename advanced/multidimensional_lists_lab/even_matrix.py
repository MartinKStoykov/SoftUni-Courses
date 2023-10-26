rows = int(input())
even_nums = []
for i in range(rows):
    even_nums.append([int(x) for x in input().split(", ") if int(x) % 2 == 0])

print(even_nums)