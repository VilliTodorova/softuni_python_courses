from sys import maxsize

number_count = int(input())
sum_numbers = 0
max_number = -maxsize

for i in range(number_count):
    current_number = int(input())

    if current_number > max_number:
        max_number = current_number

    sum_numbers += current_number

if max_number == sum_numbers - max_number:
    print("Yes")
    print(f"Sum = {max_number}")
else:
    sum_others = sum_numbers - max_number
    difference = max_number - sum_others
    print(f"No\nDiff = {abs(difference)}")
