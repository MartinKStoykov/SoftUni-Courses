import math

figure_type = input()
area = 0

if figure_type == "square":
    side_a = float(input())
    area = side_a * side_a
elif figure_type == "rectangle":
    side_a = float(input())
    side_b = float(input())
    area = side_a * side_b
elif figure_type == "circle":
    radius = float(input())
    area = radius ** 2 * math.pi
elif figure_type == "triangle":
    base = float(input())
    height = float(input())
    area = (base * height) / 2

print(f"{area:.3f}")