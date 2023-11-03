from functools import reduce
def operate(oper, *args):
    result = 0
    if oper == "+":
        return reduce(lambda a, b: a + b, args)
    elif oper == "-":
        return reduce(lambda a, b: a - b, args)
    elif oper == "*":
        return reduce(lambda a, b: a * b, args)
    elif oper == "/":
        return reduce(lambda a, b: a / b, args)