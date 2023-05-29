vegetable_price = float(input())
fruit_price = float(input())
vegetable_kg = int(input())
fruit_kg = int(input())


income = ((fruit_kg * fruit_price) + (vegetable_kg * vegetable_price)) / 1.94

print(f"{income:.2f}")