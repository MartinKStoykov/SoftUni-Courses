budget = int(input())
season = str(input())
fishermen = int(input())

boat_price = 0
if season == "Spring":
    boat_price = 3000
    if fishermen <= 6:
        boat_price *= 0.9
    elif 7 <= fishermen <= 11:
        boat_price *= 0.85
    elif fishermen >= 12:
        boat_price *= 0.75
    if fishermen % 2 == 0:
        boat_price *= 0.95
elif season == "Summer":
    boat_price = 4200
    if fishermen <= 6:
        boat_price *= 0.9
    elif 7 <= fishermen <= 11:
        boat_price *= 0.85
    elif fishermen >= 12:
        boat_price *= 0.75
    if fishermen % 2 == 0:
        boat_price *= 0.95
elif season == "Autumn":
    boat_price = 4200
    if fishermen <= 6:
        boat_price *= 0.9
    elif 7 <= fishermen <= 11:
        boat_price *= 0.85
    elif fishermen >= 12:
        boat_price *= 0.75
elif season == "Winter":
    boat_price = 2600
    if fishermen <= 6:
        boat_price *= 0.9
    elif 7 <= fishermen <= 11:
        boat_price *= 0.85
    elif fishermen >= 12:
        boat_price *= 0.75
    if fishermen % 2 == 0:
        boat_price *= 0.95
if budget >= boat_price:
    leftover_money = budget - boat_price
    print(f"Yes! You have {leftover_money:.2f} leva left.")
elif budget < boat_price:
    insufficient_money = abs(budget - boat_price)
    print(f"Not enough money! You need {insufficient_money:.2f} leva.")
