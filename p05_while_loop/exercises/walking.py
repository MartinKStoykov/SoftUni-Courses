walking_goal = 10000
total_steps = 0

while total_steps < walking_goal:
    command = input()
    if command == "Going home":
        home_steps = int(input())
        total_steps += home_steps
        break
    current_steps = int(command)
    total_steps += current_steps

if total_steps >= walking_goal:
    diff = total_steps - walking_goal
    print("Goal reached! Good job!")
    print(f"{diff} steps over the goal!")
else:
    diff = abs(total_steps - walking_goal)
    print(f"{diff} more steps to reach goal.")
