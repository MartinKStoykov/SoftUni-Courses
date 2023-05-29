flower_type = str(input())
flower_number = int(input())
budget = int(input())

flower_price = 0
price_change = 0

if flower_type == "Roses":
    flower_price = 5 * flower_number
    if flower_number > 80:
        price_change = 0.90
        flower_price *= price_change
elif flower_type == "Dahlias":
    flower_price = 3.80 * flower_number
    if flower_number > 90:
        price_change = 0.85
        flower_price *= price_change
elif flower_type == "Tulips":
    flower_price = 2.80 * flower_number
    if flower_number > 80:
        price_change = 0.85
        flower_price *= price_change
elif flower_type == "Narcissus":
    flower_price = 3 * flower_number
    if flower_number < 120:
        price_change = 1.15
        flower_price *= price_change
elif flower_type == "Gladiolus":
    flower_price = 2.50 * flower_number
    if flower_number < 80:
        price_change = 1.20
        flower_price *= price_change
if budget >= flower_price:
    left_money = budget - flower_price
    print(f"Hey, you have a great garden with {flower_number} {flower_type} and {left_money:.2f} leva left.")
elif budget < flower_price:
    insufficient_money = abs(budget - flower_price)
    print(f"Not enough money, you need {insufficient_money:.2f} leva more.")


