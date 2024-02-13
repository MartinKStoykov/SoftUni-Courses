import re

command = str(input())
total_income = 0
while command != "end of shift":
    regex = r"%([A-z][a-z]+)%[^.%$|]*<(\w+)>[^.%$|]*\|(\d+)[^.%$|]*\|[^.%$|\d]*(\d+\.?\d+)\$"
    order = re.match(regex, command)
    if order:
        print(f"{order.group(1)}: {order.group(2)} - {int(order.group(3)) * float(order.group(4)):.2f}")
        total_income += int(order.group(3)) * float(order.group(4))
    command = str(input())
print(f"Total income: {total_income:.2f}")