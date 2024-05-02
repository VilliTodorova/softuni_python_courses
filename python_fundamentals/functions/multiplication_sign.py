import math


def check_if_positive(x, y, z):
    numbers = [x, y, z]
    count_negative = 0
    for num in numbers:
        if num < 0:
            count_negative += 1
        if num == 0:
            return 'zero'

    if count_negative == 1 or count_negative == 3:
        return 'negative'
    if count_negative == 2 or count_negative == 0:
        return 'positive'


x = int(input())
y = int(input())
z = int(input())
print(check_if_positive(x, y, z))
