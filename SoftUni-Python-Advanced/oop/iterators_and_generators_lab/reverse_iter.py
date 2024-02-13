class reverse_iter:
    def __init__(self, iterable: iter):
        self.iterable = iterable
        self.curr_number = len(self.iterable)

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_number > 0:
            self.curr_number -= 1
            return self.iterable[self.curr_number]
        raise StopIteration
