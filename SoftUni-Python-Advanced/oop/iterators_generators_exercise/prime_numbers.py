def get_primes(numbers: list):

    for num in numbers:
        is_prime = True
        for n in range(2, num):
            if num % n == 0:
                is_prime = False
                break
        if is_prime and num > 1:
            yield num

