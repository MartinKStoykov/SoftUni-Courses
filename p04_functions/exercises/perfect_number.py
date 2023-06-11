def is_perfect(num):
    divisors = []
    for n in range(1, num):
        if num % n == 0:
            divisors.append(n)
    if not sum(divisors) == num:
        return False
    return True
number = int(input())
if is_perfect(number):
    print("We have a perfect number!")
else:
    print("It's not so perfect.")
