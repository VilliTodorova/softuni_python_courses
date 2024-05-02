def create_rhombus(size):
    result = ""
    for upper_row in range(1, size + 1):
        result += " " * (size - upper_row)
        result += "* " * upper_row
        result += "\n"

    for lower_row in range(size - 1, 0, -1):
        result += " " * (size - lower_row)
        result += "* " * lower_row
        result += "\n"

    return print(result)


n = int(input())

create_rhombus(n)
