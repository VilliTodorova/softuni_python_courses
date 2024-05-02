size = int(input())
airspace = []
jet_pos = []
jet_armor = 300
enemy_count = 4

for r in range(size):
    airspace.append(list(input()))

    if "J" in airspace[r]:
        c = airspace[r].index("J")
        jet_pos = [r, c]

        airspace[r][c] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

while True:

    if jet_armor <= 0:
        print(f"Mission failed, your jetfighter was shot down! Last coordinates [{jet_pos[0]}, {jet_pos[1]}]!")
        break

    command = input()

    new_row = jet_pos[0] + directions[command][0]
    new_col = jet_pos[1] + directions[command][1]

    jet_pos = [new_row, new_col]
    current_position = airspace[new_row][new_col]
    airspace[new_row][new_col] = "-"

    if current_position == "-":
        continue
    elif current_position == "R":
        jet_armor = 300
    elif current_position == "E":
        if enemy_count == 1:
            enemy_count -= 1
            print("Mission accomplished, you neutralized the aerial threat!")
            break
        else:
            jet_armor -= 100
            enemy_count -= 1

airspace[jet_pos[0]][jet_pos[1]] = "J"

for i in airspace:
    print(''.join(i))
