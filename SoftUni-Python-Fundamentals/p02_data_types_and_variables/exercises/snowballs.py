from sys import maxsize
snowballs = int(input())
max_value = -maxsize
qualities = ""
for ball in range(snowballs):
    weight = int(input())
    time_to_hit = int(input())
    quality = int(input())
    current_value = (weight / time_to_hit) ** quality
    if current_value > max_value:
        max_value = current_value
        qualities = f"{weight} : {time_to_hit} = {int(max_value)} ({quality})"
print(qualities)