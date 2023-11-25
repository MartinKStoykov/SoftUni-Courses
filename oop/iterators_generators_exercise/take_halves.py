def solution():

    def integers():
        n = 1
        while True:
            yield n
            n += 1

    def halves():
        for i in integers():
            yield i / 2

    def take(n, seq):
        sequence = []
        for i in range(n):
            sequence.append(next(seq))

        return sequence

    return (take, halves, integers)
