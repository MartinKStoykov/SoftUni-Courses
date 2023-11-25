class sequence_repeat:
    def __init__(self, sequence: str, number: int):
        self.sequence = sequence
        self.number = number
        self.count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count < self.number:
            index = self.count % len(self.sequence)
            self.count += 1
            return self.sequence[index]
        raise StopIteration

