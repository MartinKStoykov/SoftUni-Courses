kilometers = int(input())
time = str(input())
taxi_price = 0
bus_price = 0
train_price = 0
price = 0

if kilometers < 20:
    if time == "day":
        price = 0.70 + 0.79 * kilometers
    else:
        price = 0.70 + 0.90 * kilometers
elif kilometers < 100:
    price = 0.09 * kilometers
else:
    price = 0.06 * kilometers
print(f"{price:.2f}")