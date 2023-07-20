command = input()
individual_standings = {}
results = {}
while command != "no more time":
    username, contest, points = command.split(" -> ")
    if contest not in results:
        results[contest] = {username: int(points)}
    elif username not in results[contest]:
        results[contest][username] = int(points)
    elif int(points) > results[contest][username]:
        results[contest][username] = int(points)

    command = input()

for key1, value1 in results.items():
    print(f"{key1}: {len(value1)} participants")
    index = 1
    for key2, value2 in sorted(value1.items(), key=lambda kv: (-kv[1], kv[0])):
        if key2 not in individual_standings:
            individual_standings[key2] = 0

        individual_standings[key2] += value2
        print(f"{index}. {key2} <::> {value2}")
        index += 1
print("Individual standings:")
index = 1
for key, value in sorted(individual_standings.items(), key=lambda kv: (-kv[1], kv[0])):

    print(f"{index}. {key} -> {value}")
    index += 1