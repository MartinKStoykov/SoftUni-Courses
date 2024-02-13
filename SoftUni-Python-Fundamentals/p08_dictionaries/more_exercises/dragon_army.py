dragons = int(input())
dragons_found = {}
for dragon in range(dragons):
    type, name, damage, health, armor = input().split()
    if damage == "null":
        damage = 45
    if health == "null":
        health = 250
    if armor == "null":
        armor = 10
    damage = int(damage)
    health = int(health)
    armor = int(armor)
    if type not in dragons_found:
        dragons_found[type] = {}
    dragons_found[type][name] =[damage, health, armor]

for t, i in dragons_found.items():
    count = len(i)
    average_damage = sum([item[0] for item in i.values()]) / count
    average_health = sum([item[1] for item in i.values()]) / count
    average_armor = sum([item[2] for item in i.values()]) / count
    print(f"{t}::({average_damage:.2f}/{average_health:.2f}/{average_armor:.2f})")
    for d, stats in sorted(i.items(), key=lambda x: x[0]):
        print(f"-{d} -> damage: {stats[0]}, health: {stats[1]}, armor: {stats[2]}")