number = int(input())
for i in range(1, number):
    for h in range(i):
        print(f"*", end="")
    print()
print(number * "*")
for z in range(number-1, 0, -1):
    for w in range(z):
        print(f"*", end="")
    print()