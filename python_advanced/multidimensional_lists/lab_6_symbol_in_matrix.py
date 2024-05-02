size = int(input())

matrix = []

for _ in range(size):
    matrix.append(list(input()))

symbol = input()

found = False

for row_index in range(size):
    if found:
        break
    for col_index in range(size):
        if matrix[row_index][col_index] == symbol:
            print(f"({row_index}, {col_index})")
            found = True
            break
if not found:
    print(f"{symbol} does not occur in the matrix")
