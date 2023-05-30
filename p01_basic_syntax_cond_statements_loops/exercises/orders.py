order_num = int(input())
total_price = 0
for order in range(order_num):
    capsule_price = float(input())
    days = int(input())
    capsules_per_day = int(input())
    price = capsule_price * capsules_per_day * days
    if not 1 <= days <= 31 or not 0.01 <= capsule_price <= 100.00 or not 1 <= capsules_per_day <= 2000:
        continue
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
print(f"Total: ${total_price:.2f}")