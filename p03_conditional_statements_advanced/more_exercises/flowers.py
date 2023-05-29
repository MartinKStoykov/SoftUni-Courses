chrysanthemum = int(input())
rose = int(input())
tulip = int(input())
season = str(input())
day = str(input())
final_price = 0
discount = False
if chrysanthemum + rose + tulip > 20:
    discount = True
if day == "Y":
    if season == "Spring" or season == "Summer":
        final_price = (rose * 4.10 + tulip * 2.50 + chrysanthemum * 2.00) * 1.15
    elif season == "Winter" or season == "Autumn":
        final_price = (rose * 4.50 + tulip * 4.15 + chrysanthemum * 3.75) * 1.15
elif day == "N":
    if season == "Spring" or season == "Summer":
        final_price = (rose * 4.10 + tulip * 2.50 + chrysanthemum * 2.00)
    elif season == "Winter" or season == "Autumn":
        final_price = (rose * 4.50 + tulip * 4.15 + chrysanthemum * 3.75)
if tulip > 7 and season == "Spring":
    final_price *= 0.95
if rose >= 10 and season == "Winter":
    final_price *= 0.90
if discount:
    final_price *= 0.80
final_price += 2
print(f"{final_price:.2f}")