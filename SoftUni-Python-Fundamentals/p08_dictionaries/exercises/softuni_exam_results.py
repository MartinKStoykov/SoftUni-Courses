command = str(input())
exam_results = {}
submissions = {}
while command != "exam finished":
    if "banned" in command:
        name = command.split("-")[0]
        del exam_results[name]
        command = str(input())
        continue
    name, language, points = command.split("-")
    if language not in submissions:
        submissions[language] = 0
    if name not in exam_results:
        exam_results[name] = int(points)
    if exam_results[name] < int(points):
        exam_results[name] = int(points)

    submissions[language] += 1

    command = str(input())
print("Results:")
for key, value in exam_results.items():
    print(f"{key} | {value}")
print("Submissions:")
for key, value in submissions.items():
    print(f"{key} - {value}")