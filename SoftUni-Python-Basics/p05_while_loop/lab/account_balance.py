total_money = 0

while True:
    command = input()
    if command == "NoMoreMoney":
        break
    deposit_sum = float(command)
    if deposit_sum >= 0:
        total_money += deposit_sum
        print(f"Increase: {deposit_sum:.2f}")

    else:
        print("Invalid operation!")
        break

print(f"Total: {total_money:.2f}")