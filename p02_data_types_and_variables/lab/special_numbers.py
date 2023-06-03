number = int(input())
for num in range(1, number+1):
    num_sum = sum(map(int, str(num)))
    if num_sum == 5 or num_sum == 7 or num_sum == 11:
        print(f"{num} -> True")
    else:
        print(f"{num} -> False")