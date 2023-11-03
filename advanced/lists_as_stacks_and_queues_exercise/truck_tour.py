from collections import deque

pump_count = int(input())
pump_stations = deque()
for count in range(pump_count):
    pump_stations.append(input().split())
complete_circle = False
for num in range(len(pump_stations)):
    current_petrol = 0
    for pump in pump_stations:
        current_petrol += int(pump[0]) - int(pump[1])
        if current_petrol < 0:
            pump_stations.rotate(-1)
            break

    else:
        print(num)
        break