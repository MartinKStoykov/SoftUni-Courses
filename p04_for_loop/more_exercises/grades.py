students = int(input())
bad = 0
fine = 0
good = 0
great = 0
total_grades = 0
for student in range(students):
    student_grade = float(input())
    if student_grade < 3:
        bad += 1
    elif student_grade < 4:
        fine += 1
    elif student_grade < 5:
        good += 1
    else:
        great += 1
    total_grades += student_grade
print(f"Top students: {great / students * 100:.2f}%")
print(f"Between 4.00 and 4.99: {good / students * 100:.2f}%")
print(f"Between 3.00 and 3.99: {fine / students * 100:.2f}%")
print(f"Fail: {bad / students * 100:.2f}%")
print(f"Average: {total_grades / students:.2f}")