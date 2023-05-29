product = str(input())
city = str(input())
quantity = float(input())
coffee = 0
water = 0
beer = 0
sweets = 0
peanuts = 0
if city == "Sofia":
    coffee = 0.50 * quantity
    water = 0.80 * quantity
    beer = 1.20 * quantity
    sweets = 1.45 * quantity
    peanuts = 1.60 * quantity
    if product == "coffee":
        print(coffee)
    elif product == "water":
        print(water)
    elif product == "beer":
        print(beer)
    elif product == "sweets":
        print(sweets)
    elif product == "peanuts":
        print(peanuts)
elif city == "Plovdiv":
    coffee = 0.40 * quantity
    water = 0.70 * quantity
    beer = 1.15 * quantity
    sweets = 1.30 * quantity
    peanuts = 1.50 * quantity
    if product == "coffee":
        print(coffee)
    elif product == "water":
        print(water)
    elif product == "beer":
        print(beer)
    elif product == "sweets":
        print(sweets)
    elif product == "peanuts":
        print(peanuts)
elif city == "Varna":
    coffee = 0.45 * quantity
    water = 0.70 * quantity
    beer = 1.10 * quantity
    sweets = 1.35 * quantity
    peanuts = 1.55 * quantity
    if product == "coffee":
        print(coffee)
    elif product == "water":
        print(water)
    elif product == "beer":
        print(beer)
    elif product == "sweets":
        print(sweets)
    elif product == "peanuts":
        print(peanuts)