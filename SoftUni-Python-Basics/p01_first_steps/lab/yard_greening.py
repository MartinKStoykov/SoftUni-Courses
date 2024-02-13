number_of_square_meters = float(input())
price_per_square_meter = number_of_square_meters * 7.61
discount = price_per_square_meter * 0.18
final_price = price_per_square_meter - discount
print(f"The final price is: {final_price} lv.")
print(f"The discount is {discount} lv.")
