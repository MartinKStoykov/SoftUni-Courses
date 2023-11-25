class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.curr_steps = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_steps < self.count:
            self.curr_steps += 1
            return self.step * (self.curr_steps - 1)


        else:
            raise StopIteration
