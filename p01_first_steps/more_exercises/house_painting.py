x = float(input())
y = float(input())
h = float(input())

green_paint_price = 3.4
red_paint_price = 4.3

front_back_size = ((x * x) - 2.4) + x * x
side_size = (x * y * 2) - 2.25 * 2
roof_rectangles = (x * y) * 2
roof_triangle = ((h * x) / 2) * 2
green_paint = (front_back_size + side_size) / green_paint_price
red_paint = (roof_triangle + roof_rectangles) / red_paint_price
print(f"{green_paint:.2f}")
print(f"{red_paint:.2f}")