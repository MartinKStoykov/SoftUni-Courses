fruit = str(input())
day = str(input())
quantity = float(input())
price = 0
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
weekend = ["Sunday", "Saturday"]
fruit_list = ["banana", "apple", "orange", "grapefruit", "kiwi", "pineapple", "grapes"]

if day in weekdays and fruit in fruit_list:
    if fruit == "banana":
        price = 2.50 * quantity
    elif fruit == "apple":
        price = 1.20 * quantity
    elif fruit == "orange":
        price = 0.85 * quantity
    elif fruit == "grapefruit":
        price = 1.45 * quantity
    elif fruit == "kiwi":
        price = 2.70 * quantity
    elif fruit == "pineapple":
        price = 5.50 * quantity
    elif fruit == "grapes":
        price = 3.85 * quantity
    print(f"{price:.2f}")
elif day in weekend and fruit in fruit_list:
    if fruit == "banana":
        price = 2.70 * quantity
    elif fruit == "apple":
        price = 1.25 * quantity
    elif fruit == "orange":
        price = 0.90 * quantity
    elif fruit == "grapefruit":
        price = 1.60 * quantity
    elif fruit == "kiwi":
        price = 3.00 * quantity
    elif fruit == "pineapple":
        price = 5.60 * quantity
    elif fruit == "grapes":
        price = 4.20 * quantity
    print(f"{price:.2f}")

else:
    print("error")
