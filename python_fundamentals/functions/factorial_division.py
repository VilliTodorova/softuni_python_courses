def factorial_division(x, y):
    if x == 0 or y == 0:
        return 1
    else:
        factorial_x = x
        factorial_y = y
        for i in range(1, x):
            factorial_x *= i
        for i in range(1, y):
            factorial_y *= i
    division_result = factorial_x / factorial_y
    return division_result


num1 = int(input())
num2 = int(input())

result = factorial_division(num1, num2)

print(f'{result:.2f}')
