number = float(input())

if number < 0:
    if abs(number) > 1000000:
        print("large negative")
    elif abs(number) < 1 and number != 0:
        print("small negative")
    else:
        print("negative")
elif number > 0:
    if abs(number) > 1000000:
        print("large positive")
    elif abs(number) < 1 and number != 0:
        print("small positive")
    else:
        print("positive")
else:
    print("zero")

