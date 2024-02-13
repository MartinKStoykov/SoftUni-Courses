item = input().split(": ")
product_stock = {}

while item[0] != "statistics":
    product = item[0]
    quantity = int(item[1])

    if product in product_stock:
        product_stock[product] += quantity
    else:
        product_stock[product] = int(quantity)

    item = input().split(": ")

print(f"Products in stock:")

for key, value in product_stock.items():
    print(f"- {key}: {value}")

print(f"Total Products: {len(product_stock)}")
print(f"Total Quantity: {sum(product_stock.values())}")
