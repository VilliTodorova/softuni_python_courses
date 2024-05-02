your_operator = input()
num_one = int(input())
num_two = int(input())


def solve(a, b, operator):
    result = None
    if operator == 'multiply':
        result = a * b
    elif operator == 'divide':
        result = a / b
    elif operator == 'add':
        result = a + b
    elif operator == 'subtract':
        result = a - b
    return int(result)


print(solve(num_one, num_two, your_operator))
