budget = float(input())
extra_numbers = int(input())
costume_price_per_extra = float(input())

decorations = budget * 0.10
if extra_numbers > 150:
    discounted_costumes = costume_price_per_extra * 0.90
    total_costume_price = (discounted_costumes * extra_numbers)
    total_price = total_costume_price + decorations
else:
    total_costume_price = (costume_price_per_extra * extra_numbers)
    total_price = total_costume_price  + decorations

if budget < total_price:
    missing_sum = abs(budget - total_price)
    print(f"Not enough money!")
    print(f"Wingard needs {missing_sum:.2f} leva more.")
elif budget >= total_price:
    leftover_money = budget - total_price
    print(f"Action!")
    print(f"Wingard starts filming with {leftover_money:.2f} leva left.")
