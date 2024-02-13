food_per_month = float(input()) * 1000
hay_per_month = float(input()) * 1000
cover_per_month = float(input()) * 1000
guinea_pig_weight = float(input()) * 1000
enough = True
for day in range(1, 31):
    if food_per_month - 300 <= 0:
        enough = False
        break
    food_per_month -= 300
    if day % 2 == 0:
        if hay_per_month - food_per_month * 0.05 <= 0:
            enough = False
            break
        hay_per_month -= food_per_month * 0.05
    if day % 3 == 0:
        if cover_per_month - guinea_pig_weight / 3 <= 0:
            enough = False
            break
        cover_per_month -= guinea_pig_weight / 3

if enough:
    print(
        f"Everything is fine! Puppy is happy! Food: {food_per_month / 1000:.2f}, \
Hay: {hay_per_month/1000:.2f}, Cover: {(cover_per_month/1000):.2f}.")

else:
    print("Merry must go to the pet store!")