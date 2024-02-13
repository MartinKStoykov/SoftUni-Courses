month = str(input())
nights_spent = int(input())

studio = 0
apartment = 0
final_studio_price = 0
final_apartment_price = 0
studio_discount = 0
apartment_discount = 0
if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if 7 < nights_spent <= 14:
        final_studio_price = (studio * nights_spent) * 0.95
        final_apartment_price = apartment * nights_spent
    elif nights_spent > 14:
        final_studio_price = (studio * nights_spent) * 0.70
        final_apartment_price = (apartment * nights_spent) * 0.90
    else:
        final_studio_price = studio * nights_spent
        final_apartment_price = apartment * nights_spent
    print(f"Apartment: {final_apartment_price:.2f} lv.")
    print(f"Studio: {final_studio_price:.2f} lv.")
elif month == "June" or month == "September":
    studio = 75.20
    apartment = 68.70
    if nights_spent > 14:
        final_studio_price = (studio * nights_spent) * 0.80
        final_apartment_price = (apartment * nights_spent) * 0.90
    else:
        final_studio_price = studio * nights_spent
        final_apartment_price = apartment * nights_spent
    print(f"Apartment: {final_apartment_price:.2f} lv.")
    print(f"Studio: {final_studio_price:.2f} lv.")

elif month == "July" or month == "August":
    studio = 76
    apartment = 77
    if nights_spent > 14:
        final_apartment_price = (apartment * nights_spent) * 0.90
        final_studio_price = studio * nights_spent
    else:
        final_studio_price = studio * nights_spent
        final_apartment_price = apartment * nights_spent
    print(f"Apartment: {final_apartment_price:.2f} lv.")
    print(f"Studio: {final_studio_price:.2f} lv.")

