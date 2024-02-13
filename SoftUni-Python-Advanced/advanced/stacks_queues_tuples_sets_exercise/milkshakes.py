from collections import deque

chocolates = list(int(num) for num in input().split(", "))
milk_cups = deque(int(num) for num in input().split(", "))
milkshakes = 0

while chocolates and milk_cups and milkshakes < 5:
    if milk_cups[0] < 1 and chocolates[-1] < 1:
        milk_cups.popleft()
        chocolates.pop()
        continue
    elif milk_cups[0] < 1:
        milk_cups.popleft()
        continue
    elif chocolates[-1] < 1:
        chocolates.pop()
        continue
    if milk_cups[0] == chocolates[-1]:
        milk_cups.popleft()
        chocolates.pop()
        milkshakes += 1
    else:
        milk_cups.rotate(-1)
        chocolates[-1] -= 5

if milkshakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")
if chocolates:
    print(f"Chocolate: {', '.join(str(num) for num in chocolates)}")
else:
    print("Chocolate: empty")
if milk_cups:
    print(f"Milk: {', '.join(str(num) for num in milk_cups)}")
else:
    print("Milk: empty")