detergent = int(input()) * 750
pots = 0
dishes = 0
dishes_order = 1
while detergent >= 0:
    command = input()
    if command == "End":
        break
    dishes_count = int(command)
    if dishes_order == 3:
        pots += dishes_count
        detergent -= (dishes_count * 15)
        dishes_order = 1
        continue
    dishes_order += 1
    dishes += dishes_count
    detergent -= (dishes_count * 5)
if detergent >= 0:
    print("Detergent was enough!")
    print(f"{dishes} dishes and {pots} pots were washed.")
    print(f"Leftover detergent {abs(detergent)} ml.")
else:
    print(f"Not enough detergent, {abs(detergent)} ml. more necessary!")