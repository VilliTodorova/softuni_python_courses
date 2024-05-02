your_number = int(input())

for number in range(1_111, 10_000):
    number_is_special = True
    number_as_string = str(number)

    for _, digit in enumerate(number_as_string):
        digit_as_integer = int(digit)

        if digit_as_integer == 0:
            number_is_special = False
            break

        if not your_number % digit_as_integer == 0:
            number_is_special = False
            break

    if number_is_special:

        print(f"{number}", end=" ")

