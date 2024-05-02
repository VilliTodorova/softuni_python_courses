def validate(size, row, col):
    return True if row in range(0, size) and col in range(0, size) else print("Invalid coordinates")


def add_func(row, col, value):
    matrix[row][col] += value
    return matrix


def subtract_func(row, col, value):
    matrix[row][col] -= value
    return matrix


size = int(input())
matrix = [[int(x) for x in input().split()] for _ in range(size)]

command = input()

while command != "END":
    action, *nums = command.split()
    row, col = [int(x) for x in nums[:-1]]
    value = int(nums[-1])
    if action == "Add" and validate(size, row, col):
        matrix = add_func(row, col, value)
    elif action == "Subtract" and validate(size, row, col):
        matrix = subtract_func(row, col, value)

    command = input()

for r in matrix:
    print(*r, sep=" ")
    