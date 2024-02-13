fuel_type = str(input())
fuel_quantity = float(input())
card = str(input())
fuel_price = 0
if card == "Yes":
    if fuel_type == "Gas":
        fuel_price = fuel_quantity * 0.85
    elif fuel_type == "Gasoline":
        fuel_price = fuel_quantity * 2.04
    elif fuel_type == "Diesel":
        fuel_price = fuel_quantity * 2.21
else:
    if fuel_type == "Gas":
        fuel_price = fuel_quantity * 0.93
    elif fuel_type == "Gasoline":
        fuel_price = fuel_quantity * 2.22
    elif fuel_type == "Diesel":
        fuel_price = fuel_quantity * 2.33
if 20 < fuel_quantity <= 25:
    fuel_price *= 0.92
elif fuel_quantity > 25:
    fuel_price *= 0.90
print(f"{fuel_price:.2f} lv.")