def sum_numbers(a, b):
    return a + b


def subtract(result, c):
    return result - c


def add_and_subtract(a, b, c):
    result = sum_numbers(a, b)
    subtract_result = subtract(result, c)
    print(subtract_result)


a = int(input())
b = int(input())
c = int(input())

add_and_subtract(a, b, c)
