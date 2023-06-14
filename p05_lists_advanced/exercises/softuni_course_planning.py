schedule = input().split(", ")
command = input().split(":")
while command[0] != "course start":
    action = command[0]
    lesson1 = command[1]
    if action == "Add" and lesson1 not in schedule:
        schedule.append(lesson1)
    elif action == "Insert" and lesson1 not in schedule:
        schedule.insert(int(command[2]), lesson1)
    elif action == "Remove" and lesson1 in schedule:
        schedule.remove(lesson1)
        if f"{lesson1}-Exercise" in schedule:
            schedule.remove(f"{lesson1}-Exercise")
    elif action == "Swap":
        lesson2 = command[2]
        if lesson1 in schedule and lesson2 in schedule:
            first_index = schedule.index(lesson1)
            second_index = schedule.index(lesson2)
            schedule[first_index], schedule[second_index] = schedule[second_index], schedule[first_index]
            if f"{lesson1}-Exercise" in schedule and f"{lesson2}-Exercise" in schedule:
                index1 = schedule.index(f"{lesson1}-Exercise")
                index2 = schedule.index(f"{lesson2}-Exercise")
                schedule.pop(index1)
                schedule.pop(index2)
                schedule.insert(second_index+1, f"{lesson1}-Exercise")
                schedule.insert(first_index+1, f"{lesson2}-Exercise")
            elif  f"{lesson1}-Exercise" in schedule:
                index = schedule.index(f"{lesson1}-Exercise")
                schedule.pop(index)
                schedule.insert(second_index+1, f"{lesson1}-Exercise")

            elif f"{lesson2}-Exercise" in schedule:
                index = schedule.index(f"{lesson2}-Exercise")
                schedule.pop(index)
                schedule.insert(first_index+1, f"{lesson2}-Exercise")

    elif action == "Exercise" and f"{lesson1}-Exercise" not in schedule:
        if lesson1 in schedule:
            index = schedule.index(lesson1)
            schedule.insert(index+1, lesson1+"-Exercise")
        else:
            schedule.append(lesson1)
            schedule.append(lesson1 + "-Exercise")
    command = input().split(":")
for index, lesson1 in enumerate(schedule):
    print(f"{index+1}.{lesson1}")