while True:
    string = str(input())
    if string == "End":
        break
    if string == "SoftUni":
        continue
    for i in range(len(string)):
        print(string[i] * 2, end="")
    print()

