from sys import maxsize

def smallest_number(numbers):
    smallest = maxsize
    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest
numbers_list = [int(input()), int(input()), int(input())]

print(smallest_number(numbers_list))
