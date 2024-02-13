budget = float(input())
season = str(input())
destination = ""
location = ""
cost = 0
if season == "summer":
    if budget <= 100:
        destination = "Bulgaria"
        location = "Camp"
        cost = budget * 0.30
    elif budget <= 1000:
        destination = "Balkans"
        location = "Camp"
        cost = budget * 0.40
    elif budget > 1000:
        destination = "Europe"
        location = "Hotel"
        cost = budget * 0.90
elif season == "winter":
    if budget <= 100:
        destination = "Bulgaria"
        location = "Hotel"
        cost = budget * 0.70
    elif budget <= 1000:
        destination = "Balkans"
        location = "Hotel"
        cost = budget * 0.80
    elif budget > 1000:
        destination = "Europe"
        location = "Hotel"
        cost = budget * 0.90
print(f"Somewhere in {destination}")
print(f"{location} - {cost:.2f}")
