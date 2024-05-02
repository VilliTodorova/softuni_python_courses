size = int(input())
battlefield = []
sub_pos = ()

for r in range(size):
    battlefield.append(list(input()))

    if "S" in battlefield[r]:
        sub_pos = (r, battlefield[r].index("S"))
        battlefield[r][battlefield[r].index("S")] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

damage_taken = 0
ships_sunken = 0
row, col = sub_pos

while True:
    command = input()

    if damage_taken == 3:
        print(f"Mission failed, U-9 disappeared! Last known coordinates [{row}, {col}]!")
        break

    if ships_sunken == 3:
        print("Mission accomplished, U-9 has destroyed all battle cruisers of the enemy!")
        break

    new_row = row + directions[command][0]
    new_col = col + directions[command][1]

    if battlefield[new_row][new_col] == "*":
        damage_taken += 1
    elif battlefield[new_row][new_col] == "C":
        ships_sunken += 1

    battlefield[row][col] = "-"
    row, col = new_row, new_col

battlefield[row][col] = "S"

for i in battlefield:
    print("".join(i))
