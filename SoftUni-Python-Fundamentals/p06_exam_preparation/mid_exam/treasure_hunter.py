initial_loot = input().split("|")
while True:
    command = input().split()
    if command[0] == "Yohoho!":
        break
    action = command[0]
    if action == "Loot":
        for loot in command[1:]:
            if loot in initial_loot:
                continue
            initial_loot.insert(0, loot)
    elif action == "Drop":
        index = int(command[1])
        if not 0 <= index < len(initial_loot):
            continue
        initial_loot.append(initial_loot.pop(index))
    elif action == "Steal":
        index = int(command[1])
        if index >= len(initial_loot):
            print(", ".join(initial_loot))
            initial_loot.clear()
            continue
        print(", ".join(initial_loot[-index:]))
        del initial_loot[-index:]

if not initial_loot:
    print("Failed treasure hunt.")
else:
    average_treasure_gain = len("".join(initial_loot)) / len(initial_loot)
    print(f"Average treasure gain: {average_treasure_gain:.2f} pirate credits.")