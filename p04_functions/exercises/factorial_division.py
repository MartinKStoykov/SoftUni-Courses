def factorial(num1, num2):
    first_factorial = num1
    second_factorial = num2
    for num in range(num1-1, 0, -1):
        first_factorial *= num
    for num in range(num2-1, 0, -1):
        second_factorial *= num
    return f"{first_factorial / second_factorial:.2f}"



integer1 = int(input())
integer2 = int(input())
print(factorial(integer1, integer2))