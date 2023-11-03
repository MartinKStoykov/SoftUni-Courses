sequence_one = set(int(num) for num in input().split())
sequence_two = set(int(num) for num in input().split())
command_num = int(input())
for num in range(command_num):
    command = input().split()
    action = command[0] + " " + command[1]
    numbers = [int(num) for num in command[2:]]
    if action == "Add First":
        sequence_one.update(numbers)
    elif action == "Add Second":
        sequence_two.update(numbers)
    elif action == "Remove First":
        sequence_one.difference_update(numbers)
    elif action == "Remove Second":
        sequence_two.difference_update(numbers)
    elif action == "Check Subset":
        print(sequence_one.issubset(sequence_two) or sequence_two.issubset(sequence_one))

print(*sorted(sequence_one), sep=", ")
print(*sorted(sequence_two), sep=", ")

