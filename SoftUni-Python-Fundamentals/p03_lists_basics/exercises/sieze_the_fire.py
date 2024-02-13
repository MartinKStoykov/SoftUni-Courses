fires = input().split("#")
water = int(input())
effort = 0
total_fire = 0
print("Cells:")

for fire in fires:
    current_fire = fire.split(" = ")
    is_valid = (
        current_fire[0] == "High" and 81 <= int(current_fire[1]) <= 125 or
        current_fire[0] == "Medium" and 51 <= int(current_fire[1]) <= 80 or
        current_fire[0] == "Low" and 1 <= int(current_fire[1]) <= 50
    )
    if is_valid and int(current_fire[1]) <= water:
        water -= int(current_fire[1])
        effort += 0.25 * int(current_fire[1])
        total_fire += int(current_fire[1])
        print(f" - {int(current_fire[1])}")
print(f"Effort: {effort:.2f}\nTotal Fire: {total_fire}")