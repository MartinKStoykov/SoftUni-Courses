from collections import  deque
water_quantity = int(input())
command = input()
people_in_queue = deque()
while command != "Start":
    people_in_queue.append(command)
    command = input()
command = input()

while command != "End":

    if command.isdigit():
        liters_needed = int(command)
        first_person = people_in_queue.popleft()
        if liters_needed <= water_quantity:
            print(first_person, "got water")
            water_quantity -= liters_needed
        else:
            print(first_person, "must wait")
    else:
        refill = command.split()
        water_quantity += int(refill[1])
    command = input()
print(water_quantity, "liters left")