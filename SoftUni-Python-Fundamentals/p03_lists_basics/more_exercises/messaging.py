sequence_numbers = input().split()
sequence_string = list(str(input()))
final_word = ""

for num in range(len(sequence_numbers)):
    number_sum = sum(map(int, sequence_numbers[num]))
    index = - len(sequence_string) + number_sum

    final_word += f"{sequence_string[index]}"
    sequence_string.remove(sequence_string[index])

print(final_word)