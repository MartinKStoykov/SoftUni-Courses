commands_num = int(input())
parking_lot = set()
for num in range(commands_num):
    direction, number = input().split(", ")
    if direction == "IN":
        parking_lot.add(number)
    elif direction == "OUT":
        parking_lot.remove(number)

if parking_lot:
    print("\n".join(parking_lot))
else:
    print("Parking Lot is Empty")