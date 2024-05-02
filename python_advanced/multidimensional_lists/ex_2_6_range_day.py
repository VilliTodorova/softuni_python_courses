def move(direction, steps):
    r = shooter_position[0] + (directions[direction][0] * steps)
    c = shooter_position[1] + (directions[direction][1] * steps)

    if not (0 <= r < 5 and 0 <= c < 5):
        return shooter_position

    if shooting_range[r][c] == "x":
        return shooter_position

    return [r, c]


def shoot(direction):
    r = shooter_position[0] + directions[direction][0]
    c = shooter_position[1] + directions[direction][1]

    while 0 <= r < 5 and 0 <= c < 5:
        if shooting_range[r][c] == "x":
            shooting_range[r][c] = "."
            return [r, c]

        r += directions[direction][0]
        c += directions[direction][1]


shooting_range = []
shooter_position = []
free_targets = 0
shot_targets = 0
hits_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(5):
    shooting_range.append(input().split())

    if "A" in shooting_range[row]:
        shooter_position = [row, shooting_range[row].index("A")]

    free_targets += shooting_range[row].count("x")

for _ in range(int(input())):
    command = input().split()

    if command[0] == "move":
        shooter_position = move(command[1], int(command[2]))
    elif command[0] == "shoot":
        current_target = shoot(command[1])

        if current_target:
            hits_pos.append(current_target)
            shot_targets += 1

        if shot_targets == free_targets:
            print(f'Training completed! All {free_targets} targets hit.')
            break

if shot_targets < free_targets:
    print(f'Training not completed! {free_targets - shot_targets} targets left.')

print(*hits_pos, sep="\n")
