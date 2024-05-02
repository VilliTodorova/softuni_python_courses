number_count = int(input())
sum_odd = 0
sum_even = 0

for i in range(number_count):
    number = int(input())

    if i % 2 == 0:
        sum_even += number
    else:
        sum_odd += number

difference = abs(sum_odd - sum_even)
if sum_odd == sum_even:
    print(f"Yes\nSum = {sum_odd}")
else:
    print(f"No\nDiff = {difference}")
