money = float(input())
left_over_money = 0
coins = 0
while money > 0:
    money = (round(money, 2))
    if money - 2 >= 0:
        money -= 2
        coins += 1
        continue
    elif money - 1 >= 0:
        money -= 1
        coins += 1
        continue
    elif money - 0.50 >= 0:
        money -= 0.50
        coins += 1
        continue
    elif money - 0.20 >= 0:
        money -= 0.20
        coins += 1
        continue
    elif money - 0.10 >= 0:
        money -= 0.10
        coins += 1
        continue
    elif money - 0.05 >= 0:
        money -= 0.05
        coins += 1
        continue
    elif money - 0.02 >= 0:
        money -= 0.02
        coins += 1
        continue
    elif money - 0.01 >= 0:
        money -= 0.01
        coins += 1
        continue

print(coins)
