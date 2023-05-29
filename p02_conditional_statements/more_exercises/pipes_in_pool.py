v = int(input())
p1 = int(input())
p2 = int(input())
h = float(input())

filled_pool = (p1 * h) + (p2 * h)
if filled_pool > v:
    filled_pool -= v
    print(f"For {h:.2f} hours the pool overflows with {filled_pool:.2f} liters.")

else:
    percent_filled = filled_pool / v * 100
    pipe1 = p1 * h / filled_pool * 100
    pipe2 = p2 * h / filled_pool * 100
    print(f"The pool is {percent_filled:.2f}% full. Pipe 1: {pipe1:.2f}%. Pipe 2: {pipe2:.2f}%.")