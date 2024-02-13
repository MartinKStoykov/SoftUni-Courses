budget = float(input())
category = str(input())
group_size = int(input())

if group_size <= 4:
    budget *= 0.25
elif group_size <= 9:
    budget *= 0.40
elif group_size <= 24:
    budget *= 0.50
elif group_size <= 49:
    budget *= 0.60
else:
    budget *= 0.75
if category == "VIP":
    final_price = 499.99 * group_size
    diff = abs(budget - final_price)
    if budget >= final_price:
        print(f"Yes! You have {diff:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff:.2f} leva.")
elif category == "Normal":
    final_price = 249.99 * group_size
    diff = abs(budget - final_price)
    if budget >= final_price:
        print(f"Yes! You have {diff:.2f} leva left.")
    else:
        print(f"Not enough money! You need {diff:.2f} leva.")
