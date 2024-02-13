def add_and_subtract(n1, n2, n3):

    def sum_numbers(n1, n2):
        return n1 + n2
    def subtract(n1, n2):
        return n1 - n2
    return subtract(sum_numbers(n1, n2), n3)
num1 = int(input())
num2 = int(input())
num3 = int(input())
print(add_and_subtract(num1, num2, num3))