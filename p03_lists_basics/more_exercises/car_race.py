time_number = input().split(" ")
right_time = 0
left_time = 0
for number in range(len(time_number) // 2):
    if time_number[number] == "0":
        left_time *= 0.8

    left_time += int(time_number[number])

for number in range(len(time_number)-1, len(time_number) // 2, -1):
    if time_number[number] == "0":
        right_time *= 0.8

    right_time += int(time_number[number])

if right_time < left_time:
    print(f"The winner is right with total time: {right_time:.1f}")
else:
    print(f"The winner is left with total time: {left_time:.1f}")