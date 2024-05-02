
def move_rover(rover_pos, directions, command, mars):
    current_row, current_col = rover_pos
    new_row = current_row + directions[command][0]
    new_col = current_col + directions[command][1]

    new_row = (new_row + len(mars)) % len(mars)
    new_col = (new_col + len(mars)) % len(mars)

    return new_row, new_col


SIZE = 6

mars = []
rover_pos = []

for r in range(SIZE):
    mars.append(input().split())
    if "E" in mars[r]:
        rover_pos = r, mars[r].index("E")

row, col = rover_pos[0], rover_pos[1]

commands = input().split(", ")

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

resource_dict = {
    "Water deposit": 0,
    "Metal deposit": 0,
    "Concrete deposit": 0,
}

for command in commands:

    row, col = move_rover(rover_pos, directions, command, mars)
    rover_pos = (row, col)

    if mars[row][col] == "W":
        resource_dict['Water deposit'] += 1
        print(f"Water deposit found at ({row}, {col})")
    elif mars[row][col] == "M":
        resource_dict['Metal deposit'] += 1
        print(f"Metal deposit found at ({row}, {col})")
    elif mars[row][col] == "C":
        resource_dict['Concrete deposit'] += 1
        print(f"Concrete deposit found at ({row}, {col})")
    elif mars[row][col] == "R":
        print(f"Rover got broken at ({row}, {col})")
        break

if all(resource_dict.values()):
    print("Area suitable to start the colony.")
else:
    print("Area not suitable to start the colony.")