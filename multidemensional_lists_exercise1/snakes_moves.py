from collections import deque
n, m = input().split()
snake = deque(input())
for i in range(int(n)):
    curr_snake = deque()
    for j in range(int(m)):

        if i % 2 == 0:
            curr_snake.append(snake[0])
        else:
            curr_snake.appendleft(snake[0])
        snake.rotate(-1)

    print("".join(curr_snake))