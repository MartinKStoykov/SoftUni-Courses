hour_of_exam = int(input())
minute_of_exam = int(input())
arrival_hours = int(input())
arrival_minutes = int(input())
change_in_time_minutes = 0
change_in_time_hours = 0
final_minutes = 0
final_hours = 0
time_quality = ""
arrival_hour_in_minutes = arrival_hours * 60 + arrival_minutes
hour_of_exam_in_minutes = hour_of_exam * 60 + minute_of_exam

if arrival_hour_in_minutes == hour_of_exam_in_minutes:
    time_quality = "On time"
    print(time_quality)
elif arrival_hour_in_minutes < hour_of_exam_in_minutes:
    change_in_time_minutes = hour_of_exam_in_minutes - arrival_hour_in_minutes
    if change_in_time_minutes <= 30:
        time_quality = "On time"
        print(time_quality)
        print(f"{change_in_time_minutes} minutes before the start")
    else:
        time_quality = "Early"
        if change_in_time_minutes < 60:
            print(time_quality)
            print(f"{change_in_time_minutes} minutes before the start")
        elif change_in_time_minutes == 60:
            final_minutes = 0
            final_hours = 1
            print(time_quality)
            print(f"{final_hours}:{final_minutes:02d} hours before the start")
        elif change_in_time_minutes > 60:
            final_minutes = change_in_time_minutes % 60
            final_hours = change_in_time_minutes // 60
            print(time_quality)
            print(f"{final_hours}:{final_minutes:02d} hours before the start")
elif arrival_hour_in_minutes > hour_of_exam_in_minutes:
    change_in_time_minutes = arrival_hour_in_minutes - hour_of_exam_in_minutes
    time_quality = "Late"
    if change_in_time_minutes < 60:
        print(time_quality)
        print(f"{change_in_time_minutes} minutes after the start")
    elif change_in_time_minutes == 60:
        final_minutes = 0
        final_hours = 1
        print(time_quality)
        print(f"{final_hours}:{final_minutes:02d} hours after the start")
    elif change_in_time_minutes > 60:
        final_minutes = change_in_time_minutes % 60
        final_hours = change_in_time_minutes // 60
        print(time_quality)
        print(f"{final_hours}:{final_minutes:02d} hours after the start")


