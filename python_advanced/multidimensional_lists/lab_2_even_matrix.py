matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]
even_matrix = []

for i in range(len(matrix)):
    sublist = []
    for j in matrix[i]:
        if j % 2 == 0:
            sublist.append(j)
    even_matrix.append(sublist)

print(even_matrix)
