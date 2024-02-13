people = input().split()
order = int(input())
executions = []
counter = 1
index = 0
while len(people) > 0:
    if counter % order == 0:
        executions.append(int(people.pop(index)))
    else:
        index += 1
    if index >= len(people):
        index = 0
    counter += 1
print(str(executions).replace(" ", ""))