groceries = input().split("!")
command = input()
while command != "Go Shopping!":
    command = command.split()
    action = command[0]
    item1 = command[1]
    if action == "Urgent" and item1 not in groceries:
        groceries.insert(0, item1)
    elif action == "Unnecessary" and item1 in groceries:
        groceries.remove(item1)

    elif action == "Correct" and item1 in groceries:
        item2 = command[2]
        index = groceries.index(item1)
        groceries[index] = item2
    elif action == "Rearrange" and item1 in groceries:
        index = groceries.index(item1)
        groceries.append(groceries.pop(index))
    command = input()
print(", ".join(groceries))