mackerel_price = float(input())
sprinkle_price = float(input())
bonito_kg = float(input()) * (1.60 * mackerel_price)
jack_mackerel_kg = float(input()) * (1.80 * sprinkle_price)
mussels = float(input()) * 7.50
final_price = mussels + jack_mackerel_kg + bonito_kg
print(f"{final_price:.2f}")