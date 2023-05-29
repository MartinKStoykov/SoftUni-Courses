import math
days = int(input())
left_food = int(input())
daily_dog_food = float(input())
daily_cat_food = float(input())
daily_turtle_food = float(input()) / 1000

total_needed_food = days * (daily_turtle_food + daily_cat_food + daily_dog_food)
diff = abs(total_needed_food - left_food)
if total_needed_food > left_food:
    print(f"{math.ceil(diff)} more kilos of food are needed.")
else:
    print(f"{math.floor(diff)} kilos of food left.")