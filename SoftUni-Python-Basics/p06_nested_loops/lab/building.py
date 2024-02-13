floors = int(input())
rooms = int(input())
floor_type = ""
room_n = ""
for floor in range(floors, 0, -1):
    floor_type = "A" if floor % 2 else "O"
    if floor == floors:
        floor_type = "L"
    for room in range(rooms):
        room_n = f"{floor_type}{floor}{room}"
        print(room_n, end=" ")
    print()



