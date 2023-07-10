material_quantity = {"shards": 0, "fragments": 0, "motes": 0}
is_found = False
while not is_found:
    command = input().split()
    for num in range(0, len(command), 2):

        quantity = int(command[num])
        material = command[num+1].lower()
        if material not in material_quantity:
            material_quantity[material] = 0
        material_quantity[material] += quantity
        if material_quantity[material] >= 250:
            if material == "shards":
                print("Shadowmourne obtained!")
            elif material == "fragments":
                print("Valanyr obtained!")
            elif material == "motes":
                print("Dragonwrath obtained!")
            else:
                continue
            material_quantity[material] -= 250
            is_found = True
            break
for key, value in material_quantity.items():
    print(f"{key}: {value}")