lv1 = int(input())
lv2 = int(input())
lv5 = int(input())
lv_sum = int(input())
for x3 in range(lv1+1):
    for x2 in range(lv2+1):
        for x1 in range(lv5+1):
            if (1 * x3) + (2 * x2) + (5 * x1) == lv_sum:
                print(f"{x3} * 1 lv. + {x2} * 2 lv. + {x1} * 5 lv. = {lv_sum} lv.")
