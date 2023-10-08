def even_odd_filter(**kwargs):
    total_numbers = {}
    for element, nums in kwargs.items():
        if element == "odd":
            if "odd" not in total_numbers:
                total_numbers["odd"] = []
            total_numbers["odd"].extend(num for num in nums if num % 2 == 1)
        elif element == "even":
            if "even" not in total_numbers:
                total_numbers["even"] = []
            total_numbers["even"].extend(num for num in nums if num % 2 == 0)
    return {key: value for key, value in sorted(total_numbers.items())}


