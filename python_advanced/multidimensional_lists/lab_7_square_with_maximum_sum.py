from math import inf

rows, columns = [int(x) for x in input().split(", ")]

matrix = [list(int(x) for x in input().split(", ")) for _ in range(rows)]

max_sum = float(-inf)
max_sub_matrix = []

for row_index in range(rows - 1):
    for col_index in range(columns - 1):
        current_el = matrix[row_index][col_index]
        next_el = matrix[row_index][col_index + 1]
        low_el = matrix[row_index + 1][col_index]
        diagonal_el = matrix[row_index + 1][col_index + 1]
        sum_els = current_el + next_el + low_el + diagonal_el

        if max_sum <= sum_els:
            max_sum = sum_els
            max_sub_matrix = [
                [current_el, next_el],
                [low_el, diagonal_el]
            ]

print(*max_sub_matrix[0])
print(*max_sub_matrix[1])
print(max_sum)
