start = int(input())
finish = int(input())

for item in range(start, finish + 1):
    has_even_digit = False

    for index, digit in enumerate(str(item)):
        digit_as_int = int(digit)

        if digit_as_int % 2 == 0:
            has_even_digit = True
            break

    if not has_even_digit:
        print(item, end=" ")
