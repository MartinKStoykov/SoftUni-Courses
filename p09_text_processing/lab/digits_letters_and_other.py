string = str(input())
digits = [char for char in string if char.isdigit()]
letters = [char for char in string if char.isalpha()]
other = [char for char in string if not char.isalnum()]
print("".join(digits))
print("".join(letters))
print("".join(other))