def validate(indices):
    return {indices[0], indices[2]}.issubset(valid_rows) and {indices[1], indices[3]}.issubset(valid_columns)


def swap_func(command, indices):
    if len(indices) == 4 and validate(indices) and command == "swap":
        row_1, col_1, row_2, col_2 = indices
        matrix[row_1][col_1], matrix[row_2][col_2] = matrix[row_2][col_2], matrix[row_1][col_1]

        [print(*row) for row in matrix]

    else:
        print("Invalid input!")


rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

valid_rows = range(rows)
valid_columns = range(columns)

while True:
    command, *directions = [int(x) if x.isdigit() else x for x in input().split()]

    if command == "END":
        break

    swap_func(command, directions)

