operator = str(input())
a = int(input())
b = int(input())

def calculator(operator, a, b):
    if operator == "add":
        return a + b
    elif operator == "subtract":
        return a - b
    elif operator == "multiply":
        return a * b
    elif operator == "divide":
        return a / b
print(int(calculator(operator, a, b)))