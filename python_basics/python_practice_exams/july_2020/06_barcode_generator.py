start = int(input("Enter the starting number: "))
finish = int(input("Enter the ending number: "))

start_digits = [int(digit) for digit in str(start)]
finish_digits = [int(digit) for digit in str(finish)]

for i in range(len(start_digits)):
    start_digit = start_digits[i]
    finish_digit = finish_digits[i]

    for num in range(start_digit, finish_digit + 1):
        has_even_digit = False

        for digit in str(num):
            if int(digit) % 2 == 0 or digit == '0':
                has_even_digit = True
                break

        if not has_even_digit:
            print(num, end=" ")
