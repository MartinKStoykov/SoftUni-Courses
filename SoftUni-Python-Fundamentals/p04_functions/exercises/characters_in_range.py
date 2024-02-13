def character_range(char1, char2):
    character_string = ""
    for char in range(ord(char1)+1, ord(char2)):
        character_string += chr(char) + " "
    return character_string
character1 = str(input())
character2 = str(input())
print(character_range(character1, character2))
