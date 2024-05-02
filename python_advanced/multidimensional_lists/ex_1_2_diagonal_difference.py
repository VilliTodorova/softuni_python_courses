matrix = [[int(x) for x in input().split()] for _ in range(int(input()))]

primary_sum = 0
secondary_sum = 0

for n in range(len(matrix)):
    primary_sum += matrix[n][n]
    secondary_sum += matrix[n][len(matrix) - n - 1]

print(abs(primary_sum - secondary_sum))
