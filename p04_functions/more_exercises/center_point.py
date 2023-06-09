from math import floor

def distance(cord1, cord2):
    if cord1 > cord2:
        return tuple((floor(x2), floor(y2)))
    elif cord1 <= cord2:
        return tuple((floor(x1), floor(y1)))

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())

print(distance((abs(y1) + abs(x1)), abs(x2) + abs(y2)))