
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return  False


numbers = list(map(int, (input().split())))
filtered = filter(is_even, numbers)
even_list = list(filtered)
print(even_list)