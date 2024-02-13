class countdown_iterator:
    def __init__(self, count: int):
        self.count = count
        self.curr_count = count

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_count >= 0:
            self.curr_count -= 1
            return self.curr_count +1
        raise StopIteration