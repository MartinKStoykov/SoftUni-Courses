def func_executor(*args):
    executed_functions = []
    for element in args:
        executed_functions.append(f"{element[0].__name__} - {element[0](*element[1])}")

    return "\n".join(executed_functions)
def make_upper(*strings):
    result = tuple(s.upper() for s in strings)
    return result

def make_lower(*strings):
    result = tuple(s.lower() for s in strings)
    return result

print(func_executor(
    (make_upper, ("Python", "softUni")),
    (make_lower, ("PyThOn",)),
))





