input_number = int(input())
number_of_combinations = 0
for n1 in range(input_number+1):
    for n2 in range(input_number+1):
        for n3 in range(input_number+1):
            if n1 + n2 + n3 == input_number:
                number_of_combinations += 1

print(number_of_combinations)