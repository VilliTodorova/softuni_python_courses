matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]

primary_sum = 0
secondary_sum = 0
primary_mat = []
secondary_mat = []

for n in range(len(matrix)):
    primary_mat.append(str(matrix[n][n]))
    primary_sum += matrix[n][n]
    secondary_mat.append(str(matrix[n][len(matrix) - n - 1]))
    secondary_sum += matrix[n][len(matrix) - n - 1]

print(f"Primary diagonal: {', '.join(primary_mat)}. Sum: {primary_sum}\n"
      f"Secondary diagonal: {', '.join(secondary_mat)}. Sum: {secondary_sum}")

