stadium_capacity = int(input())
fan_numbers = int(input())
a = 0
b = 0
v = 0
g = 0
for fan in range(fan_numbers):
    sector = str(input())
    if sector == "A":
        a += 1
    elif sector == "B":
        b += 1
    elif sector == "V":
        v += 1
    elif sector == "G":
        g += 1
print(f"{a / fan_numbers * 100:.2f}%")
print(f"{b / fan_numbers * 100:.2f}%")
print(f"{v / fan_numbers * 100:.2f}%")
print(f"{g / fan_numbers * 100:.2f}%")
print(f"{fan_numbers / stadium_capacity * 100:.2f}%")