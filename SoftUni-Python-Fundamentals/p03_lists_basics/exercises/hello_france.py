items = input().split("|")
budget = float(input())
profit = 0
starting_money = budget
for item in items:
    current_item = item.split("->")
    can_buy = (
        current_item[0] == "Clothes" and float(current_item[1]) <= 50.00 or
        current_item[0] == "Shoes" and float(current_item[1]) <= 35.00 or
        current_item[0] == "Accessories" and float(current_item[1]) <= 20.50
    )
    if can_buy and float(current_item[1]) <= budget:
        budget -= float(current_item[1])
        profit += (float(current_item[1]) * 1.40) - float(current_item[1])
        print(f"{float(current_item[1]) * 1.4:.2f}", end=" ")
print()
print(f"Profit: {profit:.2f}")

if starting_money + profit >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")
