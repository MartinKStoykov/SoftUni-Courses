employee_info = str(input())
employee_database = {}
while employee_info != "End":
    company, employee = employee_info.split(" -> ")

    if company not in employee_database:
        employee_database[company] = []

    if employee not in employee_database[company]:
        employee_database[company].append(employee)
    employee_info = str(input())
for key, value in employee_database.items():
    print(f"{key}\n--", "\n-- ".join(value))