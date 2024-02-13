def read_next(*args):
    for arg in args:
        for element in arg:
            yield element


