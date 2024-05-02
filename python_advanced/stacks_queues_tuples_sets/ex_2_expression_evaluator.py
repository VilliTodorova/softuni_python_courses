from math import floor
from functools import reduce

expression = input().split()

index = 0

functions = {
    "*": lambda i: reduce(lambda a, b: a * b, map(int, expression[:i])),
    "+": lambda i: reduce(lambda a, b: a + b, map(int, expression[:i])),
    "-": lambda i: reduce(lambda a, b: a - b, map(int, expression[:i])),
    "/": lambda i: reduce(lambda a, b: a / b, map(int, expression[:i])),
}

while index < len(expression):
    el = expression[index]

    if el in "*+-/":
        expression[0] = functions[el](index)
        [expression.pop(1) for _ in range(index)]
        index = 1

    index += 1

print(floor(int(expression[0])))
