days = int(input())
hours = int(input())
total_tax = 0
tax = 0
for day in range(1, days+1):
    for hour in range(1, hours+1):
        if day % 2 == 0 and hour % 2 == 1:
            tax += 2.5
        elif day % 2 == 1 and hour % 2 == 0:
            tax += 1.25
        else:
            tax += 1
    total_tax += tax
    print(f"Day: {day} - {tax:.2f} leva")
    tax = 0
print(f"Total: {total_tax:.2f} leva")