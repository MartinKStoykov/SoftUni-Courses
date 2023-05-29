student_name = str(input())
student_year = 0
full_grades = 0
failed_years = 0
while True:
    yearly_grade = float(input())

    if yearly_grade < 4.00:
        failed_years += 1
        if failed_years == 2:
            print(f"{student_name} has been excluded at {student_year + 1} grade")
            break
    else:
        full_grades += yearly_grade
        student_year += 1
    if student_year == 12:
        average_grade = full_grades / student_year
        print(f"{student_name} graduated. Average grade: {average_grade:.2F}")
        break
