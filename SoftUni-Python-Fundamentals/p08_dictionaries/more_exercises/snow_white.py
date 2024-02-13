command = input()
dwarfs = {}
colors_count = {}
while command != "Once upon a time":
    name, color, physics = command.split(" <:> ")
    dwarf = f"({color}) {name}"
    if dwarf not in dwarfs:
        dwarfs[dwarf] = [color, int(physics)]
        if color not in colors_count:
            colors_count[color] = 0
        colors_count[color] += 1
    elif dwarfs[dwarf][1] < int(physics):
        dwarfs[dwarf][1] = int(physics)

    command = input()


for key, value in sorted(dwarfs.items(), key=lambda x: (x[1][1], colors_count[x[1][0]]), reverse=True):
    print(f"{key} <-> {value[1]}")