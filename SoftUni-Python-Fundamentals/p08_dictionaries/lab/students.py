student = input().split(":", 2)
student_database = {}

while len(student) > 1:
    name = student[0]
    id = student[1]
    course = student[2]

    if course not in student_database:
        student_database[course] = []

    student_database[course].append(f"{name} - {id}")
    student = input().split(":", 2)

searched_course = " ".join("".join(student).split("_"))
print("\n".join(student_database[searched_course]))