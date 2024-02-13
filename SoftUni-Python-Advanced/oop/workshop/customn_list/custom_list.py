from sys import maxsize
class CustomList:
    def __init__(self, *args):
        self.custom_list = list(args)

    def __call__(self):
        return self.custom_list

    def append(self, value: any):
        self.custom_list += [value]
        return self.custom_list

    def remove(self, index: int):
        if 0 <= index < len(self.custom_list):
            value = self.custom_list.pop(index)
            return value
        else:
            raise IndexError(f"Index {index} does not exist.")

    def get(self, index: int):
        if 0 <= index < len(self.custom_list):
            return self.custom_list[index]

        else:
            raise IndexError(f"Index {index} does not exist.")

    def extend(self, iterable: any):
        self.custom_list += iterable
        return self.custom_list

    def insert(self, index: int, value: any):
        if 0 <= index < len(self.custom_list):
            self.custom_list[index] = value
            return self.custom_list

        else:
            raise IndexError(f"Index {index} does not exist.")

    def pop(self):
        return self.custom_list.pop(-1)

    def clear(self):
        self.custom_list = []

    def index(self, value: any):
        for i, e in enumerate(self.custom_list):
            if e == value:
                return i

    def count(self, value: any):
        count = 0
        for x in self.custom_list:
            if x == value:
                count += 1
        return count

    def reverse(self):
        return self.custom_list[::-1]

    def copy(self):
        return self.custom_list

    def size(self):
        return len(self.custom_list)

    def add_first(self, value: any):
        self.custom_list = [value] + [e for e in self.custom_list]

    def dictionalize(self):
        dictionary = {}
        if len(self.custom_list) % 2 != 0:
            self.custom_list.append(" ")

            for x, y in zip(self.custom_list[::2], self.custom_list[1::2]):
                dictionary[x] = y

            self.custom_list.pop()
            return dictionary

        for x, y in zip(self.custom_list[::2], self.custom_list[1::2]):
            dictionary[x] = y
        return dictionary

    def move(self, amount: int):
        for n in range(amount):
            self.custom_list.append(self.custom_list.pop(0))

        return self.custom_list

    def sum(self):
        list_sum = 0
        for e in self.custom_list:
            if not isinstance(e, (int, float)):
                list_sum += len(e)
                continue
            list_sum += e

        return list_sum

    def overbound(self):
        max_sum = -maxsize
        for e in self.custom_list:
            if not isinstance(e, (int, float)):
                if len(e) > max_sum:
                    max_sum = len(e)

                continue
            if e > max_sum:
                max_sum = e

        return max_sum

    def underboard(self):
        min_num = maxsize
        for e in self.custom_list:
            if not isinstance(e, (int, float)):
                if len(e) < min_num:
                    min_num = len(e)

                continue
            if isinstance(e, bool):
                continue
            if e < min_num:
                min_num = e

        return min_num

