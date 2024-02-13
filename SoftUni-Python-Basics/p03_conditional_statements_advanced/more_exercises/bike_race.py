junior_racers = int(input())
veteran_racers = int(input())
terrain = str(input())
money = 0

if terrain == "trail":
    money += 5.50 * junior_racers
    money += 7 * veteran_racers
elif terrain == "cross-country":
    money += 8 * junior_racers
    money += 9.50 * veteran_racers
    if veteran_racers + junior_racers >= 50:
        money *= 0.75
elif terrain == "downhill":
    money += 12.25 * junior_racers
    money += 13.75 * veteran_racers
elif terrain == "road":
    money += 20 * junior_racers
    money += 21.50 * veteran_racers
money *= 0.95
print(f"{money:.2f}")