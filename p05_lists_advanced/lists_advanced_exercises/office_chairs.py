rooms = int(input())
difference = 0
for room in range(1, rooms+1):
    command = input().split()
    chairs = len(command[0])
    visitors = int(command[1])
    difference += visitors - chairs
    if chairs < visitors:
        print(f"{visitors-chairs} more chairs needed in room {room}")

if difference <= 0:
    print(f"Game On, {abs(difference)} free chairs left")