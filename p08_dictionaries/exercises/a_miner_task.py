resource_quantity = {}
while True:
    command = input()
    if command == "stop":
        break
    quantity = int(input())
    if command not in resource_quantity:
        resource_quantity[command] = 0
    resource_quantity[command] += quantity

for key, value in resource_quantity.items():
    print(f"{key} -> {value}")