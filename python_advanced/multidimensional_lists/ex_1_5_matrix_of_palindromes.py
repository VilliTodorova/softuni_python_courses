rows, columns = [int(x) for x in input().split()]
start = ord("a")

for r in range(start, start + rows):
    row = []

    for c in range(r, r + columns):
        row.append(f"{chr(r)}{chr(c)}{chr(r)}")

    print(*row)

