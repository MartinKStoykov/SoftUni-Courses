def rectangle(length, width):
    if type(length) != int or type(width) != int:
        return "Enter valid values!"
    def area():
        return length * width
    def perimeter():
        return 2 * (width + length)
    return f"Rectangle area: {area()}\nRectangle perimeter: {perimeter()}"