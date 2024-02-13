student_info = input().split(" : ")
courses = {}
while student_info[0] != "end":

    course = student_info[0]
    name = student_info[1]

    if course not in courses:
        courses[course] = []

    courses[course].append(name)

    student_info = input().split(" : ")
for key, value in courses.items():
    print(f"{key}: {len(value)}\n--",'\n-- '.join(value))