def fibonacci():
    numbers = [0, 1]
    while True:
        yield numbers[0]
        numbers[0], numbers[1] = numbers[1], numbers[0] + numbers[1]
        numbers.append(numbers[-2] + numbers[-1])
