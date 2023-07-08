starting_list = input().split()
bakery = {}

for element in range(0, len(starting_list), 2):
    product = starting_list[element]
    quantity = starting_list[element+1]
    bakery[product] = int(quantity)

print(bakery)