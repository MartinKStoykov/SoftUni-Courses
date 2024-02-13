lines = int(input())
tank = 255
total = 0
for line in range(lines):
    liter = int(input())
    if tank >= liter:
        tank -= liter
        total += liter
    else:
        print("Insufficient capacity!")
print(total)