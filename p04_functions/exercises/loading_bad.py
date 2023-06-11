def loading_bar(num):
    load = ""
    for percent in range(0, num, 10):
        load += "%"
    for dot in range(num, 100, 10):
        load += "."
    if "." in load:
        return f"{num}% [{load}]\nStill loading..."
    else:
        return f"{num}% Complete!\n[%%%%%%%%%%]"



integer = int(input())
print(loading_bar(integer))
