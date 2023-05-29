command = str(input())
c = False
o = False
n = False
special_numbers = 0
command_end = False
word = ""
word_done = False
while not command_end:
    while not command_end:
        if c and o and n:
            c = False
            o = False
            n = False
            print(f"{word} ", end="")
            word_done = True
        if word_done:
            word_done = False
            word = ""
        if command == "End":
            command_end = True
            break
        if not str.isalpha(command):
            command = str(input())
            continue
        if command == "c" and not c:
            c = True
            special_numbers += 1
            command = str(input())
            continue
        elif command == "o" and not o:
            o = True
            special_numbers += 1
            command = str(input())
            continue
        elif command == "n" and not n:
            n = True
            special_numbers += 1
            command = str(input())
            continue
        else:
            word += command
            command = str(input())
    special_numbers = 0
    c = False
    o = False
    n = False

