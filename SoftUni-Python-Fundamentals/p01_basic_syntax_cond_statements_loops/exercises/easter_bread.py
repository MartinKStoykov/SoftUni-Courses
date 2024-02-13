budget = float(input())
flour_kg_price = float(input())
egg_price = 0.75 * flour_kg_price
milk_price = 1.25 * flour_kg_price
loafs = 0
colored_eggs = 0
price = (flour_kg_price + egg_price + (milk_price / 4))
while True:
    if budget >= price:
        budget -= price
        colored_eggs += 3
        loafs += 1
        if loafs % 3 == 0:
            colored_eggs -= (loafs - 2)
    else:
        break
print(f"You made {loafs} loaves of Easter bread! Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")