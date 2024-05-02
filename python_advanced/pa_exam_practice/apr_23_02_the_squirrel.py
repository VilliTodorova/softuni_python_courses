def move_squirrel():
    pass


size = int(input())
field = []
squirrel_pos = []

for r in range(size):
    field.append(list(input()))

    if "s" in field[r]:
        c = field[r].index("s")
        squirrel_pos = [r, c]
        field[r][c] = "*"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, col = squirrel_pos[0], squirrel_pos[1]

hazelnuts = 0

while True:

    if hazelnuts == 3:
        print("Good job! You have collected all hazelnuts!")

    command_move = input()

    new_row = row + directions[command_move][0]
    new_col = col + directions[command_move][1]

    if field[new_row][new_col] == "*":
        continue
    elif field[new_row][new_col] == "h":
        hazelnuts += 1
    elif field[new_row][new_col] == "project":
        print("Unfortunately, the squirrel stepped on a trap...")
        break

    if not (0 <= new_row < len(field) and 0 <= new_col < len(field)):
        print("The squirrel is out of the field.")
        break
