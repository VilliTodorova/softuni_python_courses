rows, cols = (int(x) for x in input().split())
neighborhood = []

boy_pos = []
boy_initial = []

for r in range(rows):
    neighborhood.append(list(input()))

    if "B" in neighborhood[r]:
        boy_pos = r, neighborhood[r].index("B")
        boy_initial = r, neighborhood[r].index("B")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, col = boy_pos[0], boy_pos[1]

while True:

    command = input()

    row += directions[command][0]
    col += directions[command][1]

    if row not in range(rows) or col not in range(cols):
        print("The delivery is late. Order is canceled.")
        neighborhood[boy_pos[0]][boy_pos[1]] = " "
        break

    if neighborhood[row][col] == "P":
        neighborhood[row][col] = "R"
        print("Pizza is collected. 10 minutes for delivery.")
        continue

    if neighborhood[row][col] == "*":
        row -= directions[command][0]
        col -= directions[command][1]
        continue

    if neighborhood[row][col] == "A":
        print("Pizza is delivered on time! Next order...")
        neighborhood[row][col] = "P"
        break

    if neighborhood[row][col] == "-":
        neighborhood[row][col] = "."

for r in neighborhood:
    print(''.join(r))
