type_fuel = str(input())
liters = int(input())

if type_fuel != "Diesel" and type_fuel != "Gasoline" and type_fuel != "Gas":
    print(f"Invalid fuel!")
elif liters >= 25:
    print(f"You have enough {str.lower(type_fuel)}.")
elif liters < 25:
    print(f"Fill your tank with {str.lower(type_fuel)}!")
