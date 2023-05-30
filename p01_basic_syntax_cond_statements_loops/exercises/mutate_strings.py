unique = []
first_string = str(input())
second_input = str(input())
current_combo = ""
last_word = first_string
for index in range(len(first_string)):
    current_combo += f"{second_input[index:index+1]}"
    if current_combo + f"{first_string[index+1:]}" != last_word:
        current_word = current_combo + f"{first_string[index+1:]}"
        print(current_word)
        last_word = current_word