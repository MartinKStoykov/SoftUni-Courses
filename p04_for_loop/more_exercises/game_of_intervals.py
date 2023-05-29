turns = int(input())
result = 0
invalid_numbers = 0
from_0_to_9 = 0
from_10_to_19 = 0
from_20_to_29 = 0
from_30_to_39 = 0
from_40_to_50 = 0
for turn in range(turns):
    interval = int(input())
    if interval < 0 or interval > 50:
        invalid_numbers += 1
        result /= 2
    elif 0 <= interval <= 9:
        from_0_to_9 += 1
        result += interval * 0.20
    elif interval <= 19:
        from_10_to_19 += 1
        result += interval * 0.30
    elif interval <= 29:
        from_20_to_29 += 1
        result += interval * 0.40
    elif interval <= 39:
        from_30_to_39 += 1
        result += 50
    elif 40 <= interval <= 50:
        from_40_to_50 += 1
        result += 100
print(f"{result:.2f}")
print(f"From 0 to 9: {from_0_to_9 / turns * 100:.2f}%")
print(f"From 10 to 19: {from_10_to_19 / turns * 100:.2f}%")
print(f"From 20 to 29: {from_20_to_29 / turns * 100:.2f}%")
print(f"From 30 to 39: {from_30_to_39 / turns * 100:.2f}%")
print(f"From 40 to 50: {from_40_to_50 / turns * 100:.2f}%")
print(f"Invalid numbers: {invalid_numbers / turns * 100:.2f}%")