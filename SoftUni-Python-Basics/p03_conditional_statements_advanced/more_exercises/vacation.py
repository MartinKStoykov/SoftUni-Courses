budget = float(input())
season = str(input())
location = ""
accommodation = ""
if budget <= 1000:
    accommodation = "Camp"
    if season == "Summer":
        budget *= 0.65
        location = "Alaska"
    else:
        budget *= 0.45
        location = "Morocco"

elif budget <= 3000:
    accommodation = "Hut"
    if season == "Summer":
        budget *= 0.80
        location = "Alaska"
    else:
        budget *= 0.60
        location = "Morocco"
else:
    accommodation = "Hotel"
    if season == "Summer":
        budget *= 0.90
        location = "Alaska"
    else:
        budget *= 0.90
        location = "Morocco"
print(f"{location} - {accommodation} - {budget:.2f}")