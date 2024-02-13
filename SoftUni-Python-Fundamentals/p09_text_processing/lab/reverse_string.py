string = str(input())
while string != "end":
    reversed_string = string[::-1]
    print(f"{string} = {reversed_string}")
    string = str(input())
