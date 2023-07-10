command = str(input())
force_book = {}
while command != "Lumpawaroo":
    if "|" in command:
        side, user = command.split(" | ")

        if side not in force_book.keys() and not any(user in lst for lst in force_book.values()):
            force_book[side] = []
            force_book[side].append(user)

        elif not any(user in lst for lst in force_book.values()):
            force_book[side].append(user)
    elif "->" in command:
        user, side = command.split(" -> ")
        if side not in force_book.keys():
            force_book[side] = []
        if not any(user in lst for lst in force_book.values()) and side not in force_book.keys():

            force_book[side].append(user)
        elif any(user in lst for lst in force_book.values()):
            for value in force_book.values():
                if user in value:
                    value.remove(user)
            force_book[side].append(user)

        elif not any(user in lst for lst in force_book.values()):
            force_book[side].append(user)

        print(f"{user} joins the {side} side!")
    command = str(input())

for key, value in force_book.items():
    if not value:
        continue
    print(f"Side: {key}, Members: {len(value)}")
    print("!", "\n! ".join(value))