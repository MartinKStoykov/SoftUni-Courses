unwanted_grades = int(input())
grade_num = 0
grade_sum = 0
current_unwanted_grades = 0
while True:
    name_of_exam = str(input())
    if name_of_exam == "Enough":
        average_grade = grade_sum / grade_num
        print(f"Average score: {average_grade:.2f}")
        print(f"Number of problems: {grade_num}")
        print(f"Last problem: {last_problem}")
        break
    grade = int(input())
    grade_num += 1
    grade_sum += grade
    last_problem = name_of_exam


    if grade <= 4:
        current_unwanted_grades += 1
        if unwanted_grades == current_unwanted_grades:
            print(f"You need a break, {current_unwanted_grades} poor grades.")
            break
