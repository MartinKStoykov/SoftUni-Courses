from collections import deque
quantity_food = int(input())
order_queue = deque(input().split())
print(max(map(int, order_queue)))

for order in range(len(order_queue)):
    if quantity_food >= int(order_queue[0]):
        quantity_food -= int(order_queue[0])
        order_queue.popleft()

    else:
        print("Orders left:", " ".join(order_queue))
        break
else:
    print("Orders complete")
