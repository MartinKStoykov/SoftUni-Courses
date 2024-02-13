months = int(input())
water_bill = 0
internet_bill = 0
other_bills = 0
electricity_bills = 0
for month in range(months):
    current_electricity = float(input())
    water_bill += 20
    internet_bill += 15
    electricity_bills += current_electricity
    other_bills += (current_electricity + 20 + 15) * 1.20
print(f"Electricity: {electricity_bills:.2f} lv")
print(f"Water: {water_bill:.2f} lv")
print(f"Internet: {internet_bill:.2f} lv")
print(f"Other: {other_bills:.2f} lv")
print(f"Average: {(electricity_bills + water_bill + internet_bill + other_bills) / months:.2f} lv")
