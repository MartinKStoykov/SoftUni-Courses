age = int(input())
washer_price = float(input())
individual_toy_price = int(input())

number_of_toys = 0
lily_money = 00.00

for num in range(1, age+1):
    if num % 2 == 0:
        lily_money += ((num * 10) / 2) - 1.00
    else:
        number_of_toys += 1
toy_price = number_of_toys * individual_toy_price
final_money = toy_price + lily_money
diff = 0
if final_money >= washer_price:
    diff = final_money - washer_price
    print(f"Yes! {diff:.2f}")
else:
    diff = abs(final_money - washer_price)
    print(f"No! {diff:.2f}")

