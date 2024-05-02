def odd_even_sum(your_number):
    odd_sum = 0
    even_sum = 0
    for digit in str(your_number):
        digit_as_int = int(digit)
        if digit_as_int % 2 == 0:
            even_sum += digit_as_int
        else:
            odd_sum += digit_as_int
    return f"Odd sum = {odd_sum}, Even sum = {even_sum}"


your_number = int(input())

print(odd_even_sum(your_number))
