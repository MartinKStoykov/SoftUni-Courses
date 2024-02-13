free_days = int(input())
play_time_min = (free_days * 127) + (365 - free_days) * 63
time = abs(30000 - play_time_min)
hours = time // 60
minutes = time % 60
if play_time_min <= 30000:
    print(f"Tom sleeps well")
    print(f"{hours} hours and {minutes} minutes less for play")
else:
    print("Tom will run away")
    print(f"{hours} hours and {minutes} minutes more for play")