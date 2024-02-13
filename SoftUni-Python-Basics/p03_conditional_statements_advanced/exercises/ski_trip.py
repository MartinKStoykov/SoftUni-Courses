days = int(input())
room_type = str(input())
review = str(input())

final_price = 0
discount = 0
price = 0
if room_type == "room for one person":
    final_price = 18.00 * (days - 1)
elif room_type == "apartment":
    final_price = 25.00 *(days - 1)
    if days < 10:
        final_price *= 0.70
    elif 10 <= days <= 15:
        final_price *= 0.65
    else:
        final_price *= 0.50
elif room_type == "president apartment":
    final_price = 35.00 * (days - 1)
    if days < 10:
        final_price *= 0.90
    elif 10 <= days <= 15:
        final_price *= 0.85
    else:
        final_price *= 0.80

if review == "positive":
    final_price *= 1.25
else:
    final_price *= 0.90
print(f"{final_price:.2f}")