command = str(input())
while command != "Welcome!":
    house = ""
    if command == "Voldemort":
        print("You must not speak of that name!")
        break
    if len(command) < 5:
        house = "Gryffindor."
    elif len(command) == 5:
        house = "Slytherin."
    elif len(command) == 6:
        house = "Ravenclaw."
    else:
        house = "Hufflepuff."
    print(f"{command} goes to {house}")
    command = str(input())
else:
    print("Welcome to Hogwarts.")