
def valid_password(password):
    if 6 <= len(password) <= 10 and string.isalnum() and digits >= 2:
        print("Password is valid")
    if not 6 <= len(password) <= 10:
        print("Password must be between 6 and 10 characters")
    if not password.isalnum():
        print("Password must consist only of letters and digits")
    if not digits >= 2:
        print("Password must have at least 2 digits")

string = str(input())
digits = 0
for x in range(len(string)):
    if string[x].isdigit():
        digits += 1
valid_password(string)