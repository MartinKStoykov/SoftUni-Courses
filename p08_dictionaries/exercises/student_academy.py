pair_numbers = int(input())
students_grades = {}
for pair in range(pair_numbers):
    name = str(input())
    grade = float(input())
    if name not in students_grades:
        students_grades[name] = []
    students_grades[name].append(grade)

for key, value in students_grades.items():
    average_grade = sum(value) / len(value)
    if average_grade  >= 4.50:
        print(f"{key} -> {average_grade:.2f}")