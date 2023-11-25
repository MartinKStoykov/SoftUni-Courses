class dictionary_iter:
    def __init__(self, dictionary: dict):
        self.dictionary = [(key, value) for key, value in dictionary.items()]
        self.dict_count = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.dict_count < len(self.dictionary):
            self.dict_count += 1
            return self.dictionary[self.dict_count-1]
        raise StopIteration
