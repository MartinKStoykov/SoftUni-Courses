targets = list(map(int, input().split()))
command = input().split()
while command[0] != "End":
    action = command[0]
    index = int(command[1])
    value = int(command[2])
    if action == "Shoot":
        if 0 <= index < len(targets):
            targets[index] -= value
            if targets[index] <= 0:
                targets.pop(index)
    elif action == "Add":
        if 0 <= index < len(targets):
            targets.insert(index, value)
        else:
            print("Invalid placement!")
    elif action == "Strike":
        if 0 <= index-value and index+value < len(targets):
            del targets[index-value:index+value+1]

        else:
            print("Strike missed!")
    command = input().split()
targets = [str(num) for num in targets]
print("|".join(targets))