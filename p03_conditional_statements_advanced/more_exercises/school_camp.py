season = str(input())
group_type = str(input())
student_n = int(input())
nights = int(input())
sport = ""
price_per_night = 0
if season == "Winter":
    if group_type == "boys":
        price_per_night = student_n * 9.60
        sport = "Judo"
    elif group_type == "girls":
        price_per_night = student_n * 9.60
        sport = "Gymnastics"
    elif group_type == "mixed":
        price_per_night = student_n * 10
        sport = "Ski"
elif season == "Spring":
    if group_type == "boys":
        price_per_night = student_n * 7.20
        sport = "Tennis"
    elif group_type == "girls":
        price_per_night = student_n * 7.20
        sport = "Athletics"
    elif group_type == "mixed":
        price_per_night = student_n * 9.50
        sport = "Cycling"
elif season == "Summer":
    if group_type == "boys":
        price_per_night = student_n * 15
        sport = "Football"
    elif group_type == "girls":
        price_per_night = student_n * 15
        sport = "Volleyball"
    elif group_type == "mixed":
        price_per_night = student_n * 20
        sport = "Swimming"
total_price = price_per_night * nights
if student_n >= 50:
    total_price *= 0.50
elif student_n >= 20:
    total_price *= 0.85
elif student_n >= 10:
    total_price *= 0.95
print(f"{sport} {total_price:.2f} lv.")