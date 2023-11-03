student_count = int(input())
student_record = {}
for num in range(student_count):
    name, grade = input().split()
    if name not in student_record:
        student_record[name] = []
    student_record[name].append(float(grade))

for student, grades in student_record.items():
    joined_grades = " ".join(f"{grade:.2f}" for grade in grades)
    print(f"{student} -> {joined_grades} (avg: {sum(grades)/len(grades):.2f})")
