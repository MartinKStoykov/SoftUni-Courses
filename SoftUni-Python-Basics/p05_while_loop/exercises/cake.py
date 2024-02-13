cake_width = int(input())
cake_length = int(input())

cake_pieces = 0
cake_size = cake_width * cake_length
while True:
    command = input()
    if command == "STOP":
        break
    pieces_per_taking = int(command)
    cake_size -= pieces_per_taking
    if cake_size < 0:
        break
if cake_size > 0:
    print(f"{cake_size} pieces are left.")
else:
    diff = abs(cake_size)
    print(f"No more cake left! You need {diff} pieces more.")