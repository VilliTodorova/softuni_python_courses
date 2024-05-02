size = int(input())

matrix = [[int(x) for x in input().split()] for _ in range(size)]

diagonal_sum = 0

for index in range(size):
    diagonal_sum += matrix[index][index]

print(diagonal_sum)
