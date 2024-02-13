key = input().split()
message = str(input())

while message != "find":
    count = 0
    treasure_message = ""
    for char in message:
        treasure_message += chr(ord(char) - int(key[count]))

        if count+1 == len(key):
            count = 0
            continue

        count += 1
    item = treasure_message.split("&")
    location = item[2].split("<")
    print(f"Found {item[1]} at {location[1][:-1]}")
    message = str(input())
