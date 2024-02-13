from collections import deque
material_boxes = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())
toys = {}
while material_boxes and magic_levels:
    result = material_boxes[-1] * magic_levels[0]
    if result == 150:
        if "Doll" not in toys:
            toys["Doll"] = 0
        toys["Doll"] += 1
        magic_levels.popleft(), material_boxes.pop()
    elif result == 250:
        if "Wooden train" not in toys:
            toys["Wooden train"] = 0
        toys["Wooden train"] += 1
        magic_levels.popleft(), material_boxes.pop()
    elif result == 300:
        if "Teddy bear" not in toys:
            toys["Teddy bear"] = 0
        toys["Teddy bear"] += 1
        magic_levels.popleft(), material_boxes.pop()
    elif result == 400:
        if "Bicycle" not in toys:
            toys["Bicycle"] = 0
        toys["Bicycle"] += 1
        magic_levels.popleft(), material_boxes.pop()
    else:
        if magic_levels[0] == 0 and material_boxes[-1] == 0:
            magic_levels.popleft(), material_boxes.pop()
        elif magic_levels[0] == 0:
            magic_levels.popleft()
        elif material_boxes[-1] == 0:
            material_boxes.pop()
        elif result < 0:
            material_boxes.append(material_boxes.pop() + magic_levels.popleft())
        elif result > 0:
            magic_levels.popleft()
            material_boxes[-1] += 15

if ("Doll" in toys and "Train" in toys) or ("Teddy bear" in toys and "Bicycle" in toys):
    print("The presents are crafted! Merry Christmas!")
else:
    print("No presents this Christmas!")
if material_boxes:
    print(f"Materials left: {', '.join([str(x) for x in material_boxes[::-1]])}")
if magic_levels:
    print(f"Magic left: {', '.join([str(x) for x in magic_levels])}")
for key, value in sorted(toys.items()):
    print(f"{key}: {value}")