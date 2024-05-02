def positive(numbers):
    return ', '.join([num for num in numbers if int(num) >= 0])


def negative(numbers):
    return ', '.join([num for num in numbers if int(num) < 0])


def even(numbers):
    return ', '.join([num for num in numbers if int(num) % 2 == 0])


def odd(numbers):
    return ', '.join([num for num in numbers if int(num) % 2 != 0])


numbers = input().split(', ')

print(f'Positive: {positive(numbers)}')
print(f'Negative: {negative(numbers)}')
print(f'Even: {even(numbers)}')
print(f'Odd: {odd(numbers)}')
