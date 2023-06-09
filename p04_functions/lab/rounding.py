def rounding(num):
    return list(map(lambda a: round(float(a)), number))
number = input().split()
print(rounding(number))