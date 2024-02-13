cargo_n = int(input())
tons = 0
expenses = 0
bus_cargo = 0
truck_cargo = 0
train_cargo = 0
for cargo in range(cargo_n):
    weight = int(input())
    if weight <= 3:
        expenses += 200 * weight
        bus_cargo += weight
    elif weight <= 11:
        expenses += 175 * weight
        truck_cargo += weight
    else:
        expenses += 120 * weight
        train_cargo += weight
    tons += weight
print(f"{expenses / tons:.2f}")
print(f"{bus_cargo / tons * 100:.2f}%")
print(f"{truck_cargo / tons * 100:.2f}%")
print(f"{train_cargo / tons * 100:.2f}%")