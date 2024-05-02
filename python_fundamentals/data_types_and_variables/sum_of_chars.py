lines_count = int(input())
total_sum = 0

for i in range(lines_count):
    char = input()
    total_sum += ord(char)

print(f"The sum equals: {total_sum}")
