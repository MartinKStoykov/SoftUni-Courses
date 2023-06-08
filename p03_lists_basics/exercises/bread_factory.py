current_energy = 100
current_coins = 100
working_days = input().split("|")
event_failed = False
for day in working_days:
    event = day.split("-")
    if event[0] == "rest":
        initial_energy = current_energy
        current_energy += int(event[1])
        if current_energy > 100:
            current_energy = 100
        energy_gained = current_energy - initial_energy
        print(f"You gained {energy_gained} energy.")
        print(f"Current energy: {current_energy}.")
    elif event[0] == "order":
        if current_energy >= 30:
            current_energy -= 30
            current_coins += int(event[1])
            print(f"You earned {int(event[1])} coins.")
        else:
            print("You had to rest!")
            current_energy += 50
    else:
        if current_coins >= int(event[1]):
            print(f"You bought {event[0]}.")
            current_coins -= int(event[1])
        else:
            print(f"Closed! Cannot afford {event[0]}.")
            event_failed = True
            break
if not event_failed:
    print(f"Day completed!\nCoins: {current_coins}\nEnergy: {current_energy}")