from collections import deque
bees = deque(int(x) for x in input().split())
nectar = [int(x) for x in input().split()]
honey_process = deque(input().split())
honey_made = 0
while bees and nectar:
    if nectar[-1] >= bees[0]:
        honey_operator = honey_process.popleft()
        if honey_operator == "+":
            honey_made += bees.popleft() + nectar.pop()
        elif honey_operator == "-":
            honey_made += abs(bees.popleft() - nectar.pop())
        elif honey_operator == "*":
            honey_made += bees.popleft() * nectar.pop()
        else:
            if nectar[-1] == 0:
                bees.popleft(), nectar.pop()
            else:
                honey_made += bees.popleft() / nectar.pop()
    else:
        nectar.pop()
print(f"Total honey made: {honey_made}")
if bees:
    print(f"Bees left: {', '.join([str(x) for x in bees])}")
if nectar:
    print(f"Nectar left: {', '.join([str(x) for x in nectar])}")