waiting = int(input())
lifts = list(map(int, input().split()))
current_lift = 0
while waiting > 0 and sum(lifts) <= 4 * len(lifts)-1:
    if lifts[current_lift] >= 4:
        current_lift += 1
        continue
    waiting -= 1
    lifts[current_lift] += 1
if waiting != 0 and sum(lifts) == 4 * len(lifts):
    print(f"There isn't enough space! {waiting} people in a queue!")
    print(*lifts)
elif sum(lifts) != 4 * len(lifts) and waiting == 0:
    print("The lift has empty spots!")
    print(*lifts)
else:
    print(*lifts)
