from collections import deque
children = deque(input().split())
hot_toss = int(input()) - 1

while len(children) != 1:
    children.rotate(-hot_toss)
    print("Removed", children.popleft())
print("Last is", children.popleft())