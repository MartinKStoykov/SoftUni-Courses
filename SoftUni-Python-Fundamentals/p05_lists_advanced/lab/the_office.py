employee_happiness = input().split()
happiness_improvement = int(input())
improved_happiness = [int(num) * happiness_improvement for num in employee_happiness]
average_happiness = sum(improved_happiness) / len(improved_happiness)
happy_employees = [num for num in improved_happiness if int(num) >= average_happiness]
if len(happy_employees) >= len(improved_happiness) / 2:
    print(f"Score: {len(happy_employees)}/{len(improved_happiness)}. Employees are happy!")
else:
    print(f"Score: {len(happy_employees)}/{len(improved_happiness)}. Employees are not happy!")