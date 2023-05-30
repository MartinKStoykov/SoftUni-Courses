number = int(input())
for num in range(number):
    string = str(input())
    if "_" in string or "," in string or "." in string:
        print(f"{string} is not pure!")
    else:
        print(f"{string} is pure.")