string = input().split(">")
new_string = ""
explosion_strength = 0
for element in string:

    if string[0] == element:
        new_string += element

    elif element.isdigit():
        explosion_strength += int(element)
        new_string += ">"
        explosion_strength -= 1

    elif element[0].isdigit():
        new_string += ">"
        explosion_strength += int(element[0])
        for char in element:
            if explosion_strength <= 0:
                new_string += char
            else:
                explosion_strength -= 1

print(new_string)