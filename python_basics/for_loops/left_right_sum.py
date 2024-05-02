number_count = int(input())
left_sum = 0
right_sum = 0

for i in range(number_count * 2):
    numbers = int(input())
    if i < number_count:
        left_sum += numbers
    else:
        right_sum += numbers

difference = abs(left_sum - right_sum)
if left_sum == right_sum:
    print(f"Yes, sum = {left_sum}")
else:
    print(f"No, diff = {difference}")
