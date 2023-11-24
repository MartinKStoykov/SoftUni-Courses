def reverse_text(string: str):
    curr_index = len(string)
    while curr_index > 0:
        yield string[curr_index-1]
        curr_index -= 1
