class custom_range:
    def __init__(self, start: int, end: int):
        self.curr_number = start
        self.start = start
        self.end = end

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_number in range(self.start, self.end+1):
            self.curr_number += 1
            return self.curr_number - 1

        raise StopIteration