def calculator(types, product):
    if types == "int":
        return int(product) * 2
    elif types == "real":
        return f"{float(product) * 1.5:.2f}"
    elif types == "string":
        return f"${product}$"
type_value = input()
product_value = input()
print(calculator(type_value, product_value))