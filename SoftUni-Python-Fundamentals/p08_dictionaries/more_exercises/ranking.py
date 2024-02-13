contest_list = {}
ranking_list = {}


command = input()
while command != "end of contests":
    contest, password = command.split(":")
    contest_list[contest] = password
    command = input()


command = input()
while command != "end of submissions":
    contest, password, username, points = command.split("=>")

    if contest in contest_list and contest_list[contest] == password:
        if username not in ranking_list:
            ranking_list[username] = {}
        if contest not in ranking_list[username] or ranking_list[username][contest] < int(points):
            ranking_list[username][contest] = int(points)


    command = input()
top_performer = ["None", -1]
for k, v in ranking_list.items():
    current_points = 0
    for k1, v1 in v.items():
        current_points += v1
    if current_points > top_performer[1]:
        top_performer[0] = k
        top_performer[1] = current_points
print(f"Best candidate is {top_performer[0]} with total {top_performer[1]} points.\nRanking:")
for person, info in sorted(ranking_list.items()):
    print(person)
    for key, value in sorted(info.items(), key=lambda x: x[1], reverse=True):
        print(f"#  {key} -> {value}")