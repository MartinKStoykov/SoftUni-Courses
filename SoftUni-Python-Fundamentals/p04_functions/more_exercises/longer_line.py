import math

def distance(xy1, xy2, xy3, xy4):
    dist1 = math.sqrt(sum((x - y) ** 2.0 for x, y in zip(xy1, xy2)))
    dist2 = math.sqrt(sum((x - y) ** 2.0 for x, y in zip(xy3, xy4)))
    if dist1 >= dist2:
        return close_to_zero((x1, y1), (x2, y2))
    else:
        return close_to_zero((x3, y3), (x4, y4))

def close_to_zero(xy1, xy2):
    absolute1 = list(abs(num) for num in xy1)
    absolute2 = list(abs(num) for num in xy2)
    if sum(absolute1) <= sum(absolute2):
        return f"{tuple(math.floor(num) for num in xy1)}{tuple(math.floor(num) for num in xy2)}"
    else:
        return f"{tuple(math.floor(num) for num in xy2)}{tuple(math.floor(num) for num in xy1)}"

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
print(distance((x1, y1), (x2, y2), (x3, y3), (x4, y4)))