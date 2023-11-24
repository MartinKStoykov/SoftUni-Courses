def genrange(start: int, end: int):
    curr_number = start
    while curr_number <= end:
        yield curr_number
        curr_number += 1
