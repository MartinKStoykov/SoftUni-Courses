import re

dates = input()
regex = r'(\d{2})([-.\/])([A-Z][a-z]{2})\2(\d{4})\b'
valid_dates = re.findall(regex, dates)

for date in valid_dates:
    day = date[0]
    month = date[2]
    year = date[3]
    print(f"Day: {day}, Month: {month}, Year: {year}")