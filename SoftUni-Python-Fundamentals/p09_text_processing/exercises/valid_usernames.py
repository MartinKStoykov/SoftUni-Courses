usernames = input().split(", ")
for name in usernames:
    is_valid = True
    if 2 < len(name) < 17:
        for letter in name:
            if not (letter.isalnum() or letter == "-" or letter == "_"):
                is_valid = False
                break
        if is_valid:
            print(name)