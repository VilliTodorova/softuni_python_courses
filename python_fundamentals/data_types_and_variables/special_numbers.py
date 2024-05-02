your_number = int(input())

for current_num in range(1, your_number + 1):
    current_num_as_string = str(current_num)
    digits_sum = 0
    for digit in current_num_as_string:
        digits_sum += int(digit)
    is_special = False
    if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
        is_special = True
    print(f'{current_num} -> {is_special}')
