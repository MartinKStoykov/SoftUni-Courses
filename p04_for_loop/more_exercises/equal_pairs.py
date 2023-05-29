from sys import maxsize

numbers = int(input())
current_pair = 0
are_equal = True
last_pair = 0
lowest_number = maxsize
biggest_number = -maxsize
pairs = 0
for number in range(numbers):
    last_pair = current_pair
    current_pair = 0
    for _ in range(2):
        current_number = int(input())
        current_pair += current_number
        pairs += 1
    if pairs > 2:
        if last_pair == current_pair:
            are_equal = True
        else:
            are_equal = False
    pairs = 1
if are_equal:
    print(f"Yes, value={current_pair}")
else:
    diff = abs(last_pair - current_pair)
    print(f"No, maxdiff={diff}")