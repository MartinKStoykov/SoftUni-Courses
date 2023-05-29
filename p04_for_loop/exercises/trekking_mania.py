group_numbers = int(input())
peak = ""
total_players = 0

n1 = 0
n2 = 0
n3 = 0
n4 = 0
n5 = 0

for group in range(group_numbers):
    players_in_group = int(input())
    total_players += players_in_group
    if players_in_group <= 5:
        peak = "Musala"
        n1 += players_in_group
    elif players_in_group <= 12:
        peak = "Monblan"
        n2 += players_in_group
    elif players_in_group <= 25:
        peak = "Kilimanjaro"
        n3 += players_in_group
    elif players_in_group <= 40:
        peak = "K2"
        n4 += players_in_group
    elif players_in_group >= 41:
        peak = "Everest"
        n5 += players_in_group
p1 = n1 / total_players * 100
p2 = n2 / total_players * 100
p3 = n3 / total_players * 100
p4 = n4 / total_players * 100
p5 = n5 / total_players * 100

print(f"{p1:.2f}%")
print(f"{p2:.2f}%")
print(f"{p3:.2f}%")
print(f"{p4:.2f}%")
print(f"{p5:.2f}%")