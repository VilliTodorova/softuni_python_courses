matrix = [[int(x) for x in input().split(", ")] for _ in range(int(input()))]

flatten = []

for row in matrix:
    for el in row:
        flatten.append(el)

print(flatten)
