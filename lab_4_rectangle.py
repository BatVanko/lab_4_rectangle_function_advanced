def rectangle(length, width):
    def area():
        return length * width

    def perimeter():
        return 2 * length + 2 * width

    if not (isinstance(length, int) and isinstance(width, int)):
        return "Enter valid values!"
    else:
        return f"Rectangle area: {area()}"'\n'f'Rectangle perimeter: {perimeter()}'


print(rectangle('2', 10))

