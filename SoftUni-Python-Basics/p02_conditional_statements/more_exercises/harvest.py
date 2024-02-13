import math

plot_size = int(input()) * 0.40
grapes_per_square = float(input())
wine_needed = int(input())
workers = int(input())

total_grapes = plot_size * grapes_per_square
wine = (total_grapes / 2.5)
if wine < wine_needed:
    diff = abs(wine_needed - wine)
    print(f"It will be a tough winter! More {math.floor(diff)} liters wine needed.")
else:
    wine = (total_grapes / 2.5)
    print(f"Good harvest this year! Total wine: {math.floor(wine)} liters.")
    diff = abs(wine_needed - wine)
    wine -= wine_needed
    wine_per_person = (wine / workers)
    print(f"{math.ceil(diff)} liters left -> {math.ceil(wine_per_person)} liters per person.")
