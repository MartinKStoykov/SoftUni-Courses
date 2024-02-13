registration_number = int(input())
parking = {}
for reg in range(registration_number):
    command = input().split()
    action = command[0]
    name = command[1]
    if action == "register":
        plate = command[2]
        if name in parking:
            print(f"ERROR: already registered with plate number {parking[name]}")

        else:

            parking[name] = plate
            print(f"{name} registered {plate} successfully")
    elif action == "unregister":

        if name not in parking:
            print(f"ERROR: user {name} not found")

        else:
            parking.pop(name)
            print(f"{name} unregistered successfully")

for key, value in parking.items():
    print(f"{key} => {value}")