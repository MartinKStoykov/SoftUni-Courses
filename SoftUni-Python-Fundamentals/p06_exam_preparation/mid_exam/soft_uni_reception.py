students1_per_hour = int(input())
students2_per_hour = int(input())
students3_per_hour = int(input())
employee_list = [students1_per_hour, students2_per_hour, students3_per_hour]
student_count = int(input())
hours = 0
while student_count > 0:
    for employee in employee_list:
        student_count -= employee
    hours += 1
    if hours % 4 == 0:
        hours += 1
print(f"Time needed: {hours}h.")