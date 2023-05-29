import math

record_seconds = float(input())
record_length = float(input())
seconds_swam_per_metre = float(input())

seconds_for_water_resistance = math.floor(record_length / 15)
seconds_for_water_resistance_total = (seconds_for_water_resistance * 12.5)

time_for_record_ivan = seconds_swam_per_metre * record_length
total_time_ivan = time_for_record_ivan + seconds_for_water_resistance_total

if total_time_ivan < record_seconds:
    print(f"Yes, he succeeded! The new world record is {total_time_ivan:.2f} seconds.")
elif total_time_ivan >= record_seconds:
    slower_by = total_time_ivan - record_seconds
    print(f"No, he failed! He was {slower_by:.2f} seconds slower.")
