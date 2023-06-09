

def final_price(food, price):
    if food == "coffee":
        return price * 1.50
    elif food == "water":
        return  price * 1.00
    elif food == "coke":
        return  price * 1.40
    elif food == "snacks":
        return price * 2.00

product = str(input())
quantity = int(input())
print(f"{final_price(product, quantity):.2f}")
