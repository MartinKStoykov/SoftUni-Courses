projected_sum = int(input())
current_sum = 0
pay_count = 0
credit_count = 0
cash_count = 0
operation = True
cash_sum = 0
card_sum = 0
while current_sum < projected_sum:
    command = input()
    if command == "End":
        print("Failed to collect required money for charity.")
        operation = False
        break
    item_price = int(command)
    if pay_count == 1 and item_price >= 10:
        card_sum += item_price
        current_sum += item_price
        credit_count += 1
        print("Product sold!")
    elif pay_count == 0 and item_price <= 100:
        cash_sum += item_price
        current_sum += item_price
        cash_count += 1
        print("Product sold!")
    else:
        print(f"Error in transaction!")
    pay_count = 1 - pay_count
if operation:
    print(f"Average CS: {cash_sum / cash_count:.2f}")
    print(f"Average CC: {card_sum / credit_count:.2f}")