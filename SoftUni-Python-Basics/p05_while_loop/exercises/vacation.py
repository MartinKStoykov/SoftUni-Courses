needed_vacation_money = float(input())
available_money = float(input())
spending_in_a_row = 0
days = 0
while available_money < needed_vacation_money and spending_in_a_row < 5:
    action = str(input())
    money_sum = float(input())
    if action == "save":
        available_money += money_sum
        spending_in_a_row = 0
    else:
        available_money -= money_sum
        if available_money < 0:
            available_money = 0
        spending_in_a_row += 1
    days += 1
if spending_in_a_row >= 5:
    print("You can't save the money.")
    print(days)
if available_money >= needed_vacation_money:
    print(f"You saved the money for {days} days.")
