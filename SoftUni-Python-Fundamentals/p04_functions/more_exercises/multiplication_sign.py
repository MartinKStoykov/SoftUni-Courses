def multiplication_result(n1, n2, n3):


    if n1 == 0 or n2 == 0 or n3 == 0:
        return "zero"
    elif n1 > 0 and n2 > 0 and n3 > 0:
        return "positive"
    else:
        negatives = [num for num in (n1, n2, n3) if num < 0]
        if len(negatives) == 2:
            return "positive"
        else:
            return "negative"



num1 = int(input())
num2 = int(input())
num3 = int(input())

print(multiplication_result(num1, num2, num3))