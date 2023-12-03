def even_parameters(function):
    def wrapper(*args, **kwargs):
        try:
            if all(num % 2 == 0 for num in args):
                return function(*args, **kwargs)
            else:
                return "Please use only even numbers!"
        except TypeError:
            return "Please use only even numbers!"
    return wrapper


@even_parameters
def multiply(*nums):
    result = 1
    for num in nums:
        result *= num
    return result

print(multiply(2, 4, 6, 8))
print(multiply(2, 4, 9, 8))

