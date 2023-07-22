string = str(input())
new_string = ""
current_string = ""
unique_chars = []
last_digit = ""
count = 0
for char in string:
    if not char.isdigit():
        current_string += char
        if char.upper() not in unique_chars:
            unique_chars.append(char.upper())
    else:
        if count+1 <len(string) and string[count+1].isdigit():
            last_digit = char
            count += 1
            continue
        elif last_digit:
            new_string += current_string.upper() * (int(last_digit + char))
            last_digit = ""
        else:
            new_string += current_string.upper() * int(char)

        current_string = ""
    count += 1
print("Unique symbols used:", len(unique_chars))
print(new_string)