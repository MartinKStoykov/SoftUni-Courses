starting_hours = int(input())
starting_minutes = int(input())

minutes_after_change = starting_minutes + 15

if minutes_after_change >= 60:
    starting_hours += 1
if minutes_after_change >= 60:
    minutes_after_change -= 60
if starting_hours >= 24:
    starting_hours = 0

if minutes_after_change < 10:
    print(f"{starting_hours}:0{minutes_after_change}")
else:
    print(f"{starting_hours}:{minutes_after_change}")
