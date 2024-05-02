size = int(input())
matrix = [list(input()) for _ in range(size)]

a = [-2, -1, 1, 2]
positions = [(x, y) for x in a for y in a if abs(x) != abs(y)]

removed_knights = 0

while True:
    max_attacks = 0
    pos_max_knight = []

    for row in range(size):
        for col in range(size):
            if matrix[row][col] == "K":
                attacks = 0

                for pos in positions:
                    pos_row = row + pos[0]
                    pos_col = col + pos[1]

                    if 0 <= pos_row < size and 0 <= pos_col < size:
                        if matrix[pos_row][pos_col] == "K":
                            attacks += 1

                if attacks > max_attacks:
                    pos_max_knight = [row, col]
                    max_attacks = attacks

    if pos_max_knight:
        r, c = pos_max_knight
        matrix[r][c] = "0"
        removed_knights += 1
    else:
        break

print(removed_knights)
