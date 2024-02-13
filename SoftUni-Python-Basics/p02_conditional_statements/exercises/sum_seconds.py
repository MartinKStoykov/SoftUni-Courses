time_first = int(input())
time_second = int(input())
time_third = int(input())

time_sum = (time_third + time_second + time_first)
minutes = int(time_sum / 60)
seconds = time_sum % 60

if seconds < 10:
    print(f"{minutes}:0{seconds}")
else:
    print(f"{minutes}:{seconds}")
