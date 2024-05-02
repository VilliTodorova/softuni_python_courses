def move_player(matrix, player_pos, moves_counter, *direction):
    new_row = player_pos[0] + direction[0]
    new_col = player_pos[1] + direction[1]

    if not (0 <= new_row < len(matrix) and 0 <= new_col < len(matrix)) or matrix[new_row][new_col] == "O":
        new_row = player_pos[0]
        new_col = player_pos[1]
    else:
        moves_counter += 1

    return new_row, new_col, moves_counter


rows, cols = (map(int, input().split()))
playground = []
blind_man_pos = []

for r in range(rows):
    playground.append(input().split())

    if "B" in playground[r]:
        c = playground[r].index("B")
        blind_man_pos = [r, c]
        playground[r][c] = "-"

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1)
}

row, col = blind_man_pos[0], blind_man_pos[1]

touched_players = 0
moves_made = 0

command = input()

while command != "Finish":

    if touched_players == 3:
        break

    row, col, moves_made = move_player(playground, (row, col), moves_made, *directions[command])

    if playground[row][col] == "P":
        touched_players += 1
        playground[row][col] = "-"

    command = input()

print("Game over!")
print(f"Touched opponents: {touched_players} Moves made: {moves_made}")
