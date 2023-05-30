coffee = 0
while True:
    command = str(input())
    if command == "END":
        break
    casef = command.casefold()
    if casef != "coding" and casef != "cat" and casef != "dog" and casef != "movie":
        continue
    if command.isupper():
        coffee += 2
    else:
        coffee += 1
if coffee > 5:
    print(f"You need extra sleep")
else:
    print(coffee)
