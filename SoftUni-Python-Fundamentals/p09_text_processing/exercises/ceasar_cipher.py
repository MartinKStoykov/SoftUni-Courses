starting_text = str(input())
for sign in starting_text:
    new_ascii_value = ord(sign)+3
    print(chr(new_ascii_value), end="")