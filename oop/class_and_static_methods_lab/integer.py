from math import floor
class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, float_value: float):
        if isinstance(float_value, float):
            return cls(floor(float_value))
        return "value is not a float"
    @classmethod
    def from_roman(cls, value: str):
        roman_numbers = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        total_sum = 0
        for char in range(len(value)):
            try:
                if roman_numbers[value[char]] < roman_numbers[value[char+1]]:
                    total_sum -= roman_numbers[value[char]]

                else:
                    total_sum += roman_numbers[value[char]]

            except IndexError:
                return cls(total_sum + roman_numbers[value[char]])

    @classmethod
    def from_string(cls, value: str):
        if isinstance(value, str):
            return cls(int(value))
        return "wrong type"

first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))
