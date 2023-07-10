countries = input().split(", ")
capitals = input().split(", ")
result = zip(countries, capitals)
for country, capital in result:
    print(f"{country} -> {capital}")