n = int(input())
total = 0
for numbers in range(n):
    number = int(input())
    total += number
print(f"{total / n:.2f}")