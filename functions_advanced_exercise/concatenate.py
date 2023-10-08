def concatenate(*args, **kwargs):
    new_string = "".join(string for string in args)
    for key, value in kwargs.items():
        if key in new_string:
            new_string = new_string.replace(key, value)

    return new_string
