w = float(input())
h = float(input()) - 1.00
full_size = w * h
working_space_w = w // (120 / 100)
working_space_h = h // (70 / 100)
full_working_space = (working_space_h * working_space_w) - 3
print(int(full_working_space))
