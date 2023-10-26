from collections import deque
available_robots = deque(input().split(";"))
start_time = input().split(":")
product_queue = deque()
busy_robots = {}
if len(start_time[0]) == 1:
    start_time[0] = "0" + start_time[0]
start_time[2] = str(int(start_time[2]) + 1)
time_passed = 0
ended = False
for hour in range(int(start_time[0]), 24):
    for minute in range(int(start_time[1]), 60):
        for second in range(int(start_time[2]), 60):
            if str(time_passed) in busy_robots:
                available_robots.appendleft(busy_robots.pop(str(time_passed)))
            if not ended:
                product_queue.append(input())
                if product_queue[-1] == "End":
                    ended = True
            if available_robots:
                print(f"{available_robots[0]} - {product_queue[0]} [{hour}:{minute}:{second}]")
                name, process_time = available_robots[0].split("-")
                busy_robots[process_time] = name
                available_robots.popleft()
            time_passed += 1
        time_passed += 1
    time_passed += 1