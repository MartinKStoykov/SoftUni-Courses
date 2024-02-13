from typing import List

class Stack:
    def __init__(self):
        self.data: List[str] = []

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return not len(self.data)

    def __str__(self):
        return f"[{', '.join([el for el in reversed(self.data)])}]"