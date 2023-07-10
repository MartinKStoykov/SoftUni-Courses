orders = {}
while True:
    product_info = input().split()
    name = product_info[0]
    if name == "buy":
        break
    price = float(product_info[1])
    quantity = int(product_info[2])
    if name not in orders:
        orders[name] = [price, quantity]

    else:
        orders[name][0] = price
        orders[name][1] += quantity

for key, value in orders.items():
    total = value[0] * value[1]
    print(f"{key} -> {total:.2f}")