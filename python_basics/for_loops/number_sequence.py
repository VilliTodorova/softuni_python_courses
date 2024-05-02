import sys
numbers_count = int(input())
max_number = -sys.maxsize
min_number = sys.maxsize

for i in range(numbers_count):
    number = int(input())
    if number > max_number:
        max_number = number
    if number < min_number:
        min_number = number

print(f"Max number: {max_number}\nMin number: {min_number}")
