destination_country = str(input())
min_budget_for_destination = float(input())
added_money = 0
running_vacations = True
vacation_end = False
while not vacation_end:
    while running_vacations:
        added_money += float(input())
        if added_money >= min_budget_for_destination:
            print(f"Going to {destination_country}!")
            destination_country = str(input())
            if destination_country == "End":
                vacation_end = True
                running_vacations = False
                break
            min_budget_for_destination = float(input())
            added_money = 0
