
square_meters = int(input())
paint_litres = int(input())
thinner_litres = int(input())
number_hours_worked = int(input())


nylon_price_per_square_meter = 1.50
paint_price_per_litre = 14.50
paint_thinner_price_per_litre = 5.00
bags_price = 0.40

nylon_final_price = square_meters * nylon_price_per_square_meter + (2 * nylon_price_per_square_meter)
paint_final_price = paint_litres * paint_price_per_litre + ((paint_litres * 0.10) * paint_price_per_litre)
thinner_final_price = thinner_litres * paint_thinner_price_per_litre

total_sum = thinner_final_price + paint_final_price + nylon_final_price + bags_price

price_for_workers = (total_sum * 0.30) * number_hours_worked
final_price = price_for_workers + total_sum

print(final_price)