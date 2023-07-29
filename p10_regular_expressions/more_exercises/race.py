import re

racers = input().split(", ")
race_statistics = {}
command = str(input())
while command != "end of race":
    name = "".join(re.findall(r"[A-Za-z]+", command))
    distance = sum(map(int, re.findall(r"\d", command)))
    if name in racers:
        if name not in race_statistics:
            race_statistics[name] = 0
        race_statistics[name] += distance

    command = str(input())

sorted_list = sorted(race_statistics.items(), key=lambda x: x[1], reverse=True)
print(f"1st place: {sorted_list[0][0]}")
print(f"2nd place: {sorted_list[1][0]}")
print(f"3rd place: {sorted_list[2][0]}")