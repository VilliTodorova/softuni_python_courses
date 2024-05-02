# numbers = input().split()
# even_numbers = list(filter(lambda x: int(x) % 2 == 0, numbers))
# even_as_int = list(map(int, even_numbers))
# print(even_as_int)


def is_even(x):
    return int(x) % 2 == 0


numbers = input().split()
even_numbers = list(filter(is_even, numbers))
even_as_int = list(map(int, even_numbers))
print(even_as_int)
