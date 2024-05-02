rows, cols = [int(x) for x in input().split(",")]

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

cupboard = []
mouse_pos = ()
cheese_available = 0

for r in range(rows):
    cupboard.append(list(input()))
    if "M" in cupboard[r]:
        mouse_pos = (r, cupboard[r].index("M"))
        cupboard[mouse_pos[0]][mouse_pos[1]] = "*"
    cheese_available += cupboard[r].count("C")

row, col = mouse_pos

while True:
    command = input()

    if command == "danger":
        if cheese_available > 0:
            print("Mouse will come back later!")
            cupboard[row][col] = "M"
            break

    if cheese_available == 0:
        print("Happy mouse! All the cheese is eaten, good night!")
        cupboard[row][col] = "M"
        break

    row += directions[command][0]
    col += directions[command][1]
    mouse_pos = (row, col)

    if not (0 <= row < rows and 0 <= col < cols):
        print("No more cheese for tonight!")
        cupboard[row - directions[command][0]][col - directions[command][1]] = "M"
        break

    if cupboard[row][col] == "C":
        cupboard[row][col] = "*"
        cheese_available -= 1

    if cupboard[row][col] == "T":
        print("Mouse is trapped!")
        cupboard[row][col] = "M"
        break

    if cupboard[row][col] == "@":
        row = mouse_pos[0] - directions[command][0]
        col = mouse_pos[1] - directions[command][1]
        continue

print(*["".join(x) for x in cupboard], sep="\n")
