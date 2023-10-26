def grocery_store(**kwargs):
    sorted_list = [f"{product}: {price}"for product, price in sorted(kwargs.items(), key=lambda kvp: \
        (-kvp[1], -(len(kvp[0])), kvp[0]))]
    return "\n".join(sorted_list)

print(grocery_store(
    bread=2,
    pasta=2,
    eggs=20,
    carrot=1,
))
