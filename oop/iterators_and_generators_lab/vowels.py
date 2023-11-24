class vowels:
    def __init__(self, text: str):
        self.curr_index = 0
        self.text = text
        self.found_vowels = [v for v in self.text if v in "aeyuioAEYUIO"]

    def __iter__(self):
        return self

    def __next__(self):
        if self.curr_index >= len(self.found_vowels):
            raise StopIteration

        self.curr_index += 1
        return self.found_vowels[self.curr_index-1]