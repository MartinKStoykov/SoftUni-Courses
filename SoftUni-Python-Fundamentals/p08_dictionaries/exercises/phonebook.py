command = input()
phonebook = {}
while "-" in command:
    person, number = command.split("-")
    phonebook[person] = number
    command = input()

for num in range(int(command)):
    searched_name = str(input())
    if searched_name in phonebook:
        print(f"{searched_name} -> {phonebook[searched_name]}")

    else:
        print(f"Contact {searched_name} does not exist.")