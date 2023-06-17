def take_and_skip(string, take, skip):
    num_count = len(take)
    new_string = []
    for i in range(num_count):
        new_string.extend(string[:take[i]])
        del string[:take[i]]
        del string[:skip[i]]
        if "" in new_string:
            new_string.remove("")
    return new_string

starting_string = list(str(input()))
numbers_list = [int(num) for num in starting_string if num.isdigit()]
character_string = [char for char in starting_string if not char.isdigit()]
take_list = [numbers_list[num] for num in range(len(numbers_list)) if num % 2 == 0]
skip_list = [numbers_list[num] for num in range(len(numbers_list)) if num % 2 != 0]
print("".join(take_and_skip(character_string, take_list, skip_list)))