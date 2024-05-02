rows, columns = [int(x) for x in input().split()]
matrix = [[int(x) for x in input().split()] for _ in range(rows)]

max_matrix = []
max_sum = float("-inf")

for r in range(rows - 2):
    for c in range(columns - 2):
        first_row = matrix[r][c:c+3]
        second_row = matrix[r+1][c:c+3]
        third_row = matrix[r+2][c:c+3]

        sub_sum = sum(first_row) + sum(second_row) + sum(third_row)

        if sub_sum > max_sum:
            max_sum = sub_sum
            max_matrix = f"{' '.join(map(str, first_row))}\n" \
                         f"{' '.join(map(str, second_row))}\n" \
                         f"{' '.join(map(str, third_row))}"

print(f"Sum = {max_sum}")
print(max_matrix)
