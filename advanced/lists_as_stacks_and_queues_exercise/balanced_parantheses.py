from collections import deque
sequence = input()
par_list = deque()
for char in sequence:
    if par_list and char in ["]", "}", ")"]:
        if par_list[-1] + char not in ["()", "{}", "[]"]:
            break
        par_list.pop()
        continue
    par_list.append(char)
if not par_list:
    print("YES")
else:
    print("NO")