from collections import deque
expression = deque(input().split())
current_numbers = deque()
for char in expression:
    if char.lstrip("-").isdigit():
        current_numbers.append(int(char))

    elif char == "*":
        current_sum = current_numbers.popleft()
        while current_numbers:
            current_sum *= current_numbers.popleft()
        current_numbers.append(current_sum)
    elif char == "-":
        current_sum = current_numbers.popleft()
        while current_numbers:
            current_sum -= current_numbers.popleft()
        current_numbers.append(current_sum)
    elif char == "+":
        current_sum = current_numbers.popleft()
        while current_numbers:
            current_sum += current_numbers.popleft()
        current_numbers.append(current_sum)
    elif char == "/":
        current_sum = current_numbers.popleft()
        while current_numbers:
            current_sum //= current_numbers.popleft()
        current_numbers.append(current_sum)

print(*current_numbers)