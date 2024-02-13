stack = []
query_count = int(input())

for query in range(query_count):
    command = input().split()
    if len(command) == 2:
        stack.append(int(command[1]))

    elif command[0] == "2" and stack:
        stack.pop()

    elif command[0] == "3" and stack:
        print(max(stack))

    elif command[0] == "4" and stack:
        print(min(stack))

final_stack = [str(num) for num in stack[::-1]]
print(", ".join(final_stack))