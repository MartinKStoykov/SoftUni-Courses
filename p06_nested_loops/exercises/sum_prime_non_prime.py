is_operation_running = True
is_prime = True
prime_numbers = 0
non_prime_numbers = 0
while is_operation_running:
    command = input()
    if command == "stop":
        is_operation_running = False
        break
    current_number = int(command)
    if current_number < 0:
        print("Number is negative.")
        continue
    else:
        for i in range(2, current_number):
            if current_number % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers += current_number
        else:
            non_prime_numbers += current_number
            is_prime = True
print(f"Sum of all prime numbers is: {prime_numbers}")
print(f"Sum of all non prime numbers is: {non_prime_numbers}")

