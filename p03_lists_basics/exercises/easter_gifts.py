gift_list = input().split(" ")
command = str(input())
final_list = ""

while command != "No Money":
    action = command.split(" ")

    if action[0] == "OutOfStock":
        for index in range(len(gift_list)):
            if gift_list[index] == action[1]:
                gift_list[int(index)] = "None"
    elif action[0] == "Required":
        if len(gift_list) >= int(action[2]) >= 0:
            gift_list[int(action[2])] = action[1]
    elif action[0] == "JustInCase":
        gift_list[-1] = action[1]
    command = str(input())

for gift in gift_list:
    if gift != "None":
        final_list += gift + " "

print(final_list)