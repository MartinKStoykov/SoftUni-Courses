import re

command = input()
regex = r">>([A-Za-z]+)<<(\d+\.?\d+)!(\d+)$"
items = []
cost = 0
while command != "Purchase":
    furniture_found = re.findall(regex,command)
    if furniture_found:
        items.append(furniture_found[0][0])
        cost += (float(furniture_found[0][1]) * int(furniture_found[0][2]))
    command = input()
print("Bought furniture:")
if items:
    print("\n".join(items))
print(f"Total money spend: {cost:.2f}")