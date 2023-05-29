width_free_space = int(input())
length_free_space = int(input())
height_free_space = int(input())
operation_is_running = True
free_space = height_free_space * length_free_space * width_free_space

while free_space > 0:
    command = input()
    if command == "Done":
        operation_is_running = False
        break
    current_boxes = int(command)
    if free_space > 0:
        free_space -= current_boxes

if not operation_is_running:
    print(f"{free_space} Cubic meters left.")
if free_space <= 0:
    diff = abs(free_space)
    print(f"No more free space! You need {diff} Cubic meters more.")
