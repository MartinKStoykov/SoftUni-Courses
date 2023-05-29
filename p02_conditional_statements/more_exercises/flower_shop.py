import math

magnoli = int(input())
zyumbyuli = int(input())
roses = int(input())
cactus = int(input())
present_price = float(input())
magnoli_price = 3.25
zyumbyuli_price = 4
roses_price = 3.50
cactus_price = 8
i = ((magnoli * magnoli_price) + (zyumbyuli_price * zyumbyuli) + (cactus_price * cactus) + (roses_price * roses)) * 0.95
diff = abs(i - present_price)
if i >= present_price:
    print(f"She is left with {math.floor(diff)} leva.")
else:
    print(f"She will have to borrow {math.ceil(diff)} leva.")