import sys

biggest_number = -sys.maxsize

while True:
    command = input()
    if command == "Stop":
        print(biggest_number)
        break
    number = int(command)
    if number > biggest_number:
        biggest_number = number