clothes = input().split()
rack_capacity = int(input())
used_racks = 1
current_clothes = []
while clothes:
    for cloth in clothes:
        current_clothes.append(int(clothes.pop()))
        if sum(current_clothes) == rack_capacity:
            if clothes:
                used_racks += 1
            current_clothes = []
        elif sum(current_clothes) > rack_capacity:
            used_racks += 1
            current_clothes = [current_clothes[-1]]
print(used_racks)