price_of_excursion = float(input())
number_puzzles = int(input())
number_dolls = int(input())
number_teddies = int(input())
number_minions = int(input())
number_trucks = int(input())

puzzle_price = 2.60
talking_doll = 3
teddy_bear = 4.10
minion = 8.20
toy_truck = 2

final_puzzle_price = number_puzzles * puzzle_price
final_dolls_price = number_dolls * talking_doll
final_teddy_price = number_teddies * teddy_bear
final_minion_price = number_minions * minion
final_truck_price = number_trucks * toy_truck

final_price = final_truck_price + final_minion_price + final_teddy_price + final_dolls_price + final_puzzle_price
total_purchases = number_puzzles + number_trucks + number_teddies + number_dolls + number_minions
if total_purchases >= 50:
    final_price *= 0.75
earnings = final_price * 0.90

if earnings >= price_of_excursion:
    earnings -= price_of_excursion
    print(f"Yes! {earnings:.2f} lv left.")
elif earnings < price_of_excursion:
    earnings = abs(earnings - price_of_excursion)
    print(f"Not enough money! {earnings:.2f} lv needed.")
