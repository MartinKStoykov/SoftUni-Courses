from collections import deque
customers = deque()
name = input()

while name != "End":
    if name == "Paid":
        while customers:
            print(customers.popleft())
    else:
        customers.append(name)
    name = input()

print(len(customers), "people remaining.")