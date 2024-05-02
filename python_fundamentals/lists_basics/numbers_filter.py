n = int(input())
all_numbers = []
filtered_nums = []

for _ in range(n):
    current_num = int(input())
    all_numbers.append(current_num)

command = input()
if command == "even":
    for number in all_numbers:
        if number % 2 == 0:
            filtered_nums.append(number)
elif command == "odd":
    for number in all_numbers:
        if number % 2 != 0:
            filtered_nums.append(number)
elif command == "negative":
    for number in all_numbers:
        if number < 0:
            filtered_nums.append(number)
elif command == "positive":
    for number in all_numbers:
        if number >= 0:
            filtered_nums.append(number)

print(filtered_nums)
