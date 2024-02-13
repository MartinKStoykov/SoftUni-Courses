budget = int(input())
command = input()
while command != "End":
    item = int(command)
    if budget < item:
        print(f"You went in overdraft!")
        break
    budget -= item
    command = input()
else:
    print("You bought everything needed.")