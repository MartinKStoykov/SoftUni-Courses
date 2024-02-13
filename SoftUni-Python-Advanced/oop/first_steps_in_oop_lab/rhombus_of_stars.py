rhombus_size = int(input())


def form_rhombus_row(n, row):
    return " " * (n - row) + "* " * row + "\n"


def form_upper_rhombus(n):
    result = ""
    for row in range(1, n):
        result += form_rhombus_row(n, row)

    return result


def form_lower_rhombus(n):
    result = ""
    for row in range(n-1, 0, -1):
        result += form_rhombus_row(n, row)

    return result


def form_middle_rhombus(n):
    return form_rhombus_row(n, n)


print(form_upper_rhombus(rhombus_size) + form_middle_rhombus(rhombus_size) + form_lower_rhombus(rhombus_size))