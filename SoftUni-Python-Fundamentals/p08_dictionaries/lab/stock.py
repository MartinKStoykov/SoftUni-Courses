starting_list = input().split()
product_stock = {}

for item in range(0, len(starting_list), 2):
    product = starting_list[item]
    quantity = starting_list[item+1]
    product_stock[product] = int(quantity)

searched_products = input().split()

for product in searched_products:

    if product in product_stock:
        print(f"We have {product_stock[product]} of {product} left")
    else:
        print(f"Sorry, we don't have {product}")

