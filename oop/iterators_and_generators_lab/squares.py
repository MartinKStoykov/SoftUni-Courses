def squares(count):
    curr_number = 1
    while curr_number <= count:
        yield curr_number ** 2
        curr_number += 1
