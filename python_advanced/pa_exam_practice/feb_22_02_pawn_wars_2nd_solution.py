def label_squares(column, row):
    start_ascii = 97
    col_letter = chr(start_ascii + column)
    row_num = 9 - row

    return f"{col_letter}{row_num}"


def check_queen_promotion(white_p, black_p):
    square = ""
    winner = ""

    if white_p[0] == 0:
        winner = "White"
        square = f"{label_squares(white_p[1], white_p[0] + 1)}"
    elif black_p[0] == 7:
        winner = "Black"
        square = f"{label_squares(black_p[1], black_p[0] + 1)}"

    if winner:
        return f"Game over! {winner} pawn is promoted to a queen at {square}."
    return None


def move_pawns(current_row, pawn):
    if pawn == "White":
        current_row -= 1
    elif pawn == "Black":
        current_row += 1

    return current_row


board = []
white_pos = []
black_pos = []

for r in range(8):
    board.append(input().split())

    if "w" in board[r]:
        white_pos = [r, board[r].index("w")]
    elif "b" in board[r]:
        black_pos = [r, board[r].index("b")]

turn = 1

while True:

    w_r, w_c = white_pos
    b_r, b_c = black_pos

    result = check_queen_promotion(white_pos, black_pos)
    if result:
        print(result)
        break

    pawn_to_move = ""

    if turn % 2 != 0:  # White's turn
        pawn_to_move = "White"
        if b_r == w_r - 1 and (b_c == w_c + 1 or b_c == w_c - 1):
            print(f"Game over! White win, capture on {label_squares(b_c, b_r + 1)}.")
            break
        else:
            w_r = move_pawns(w_r, pawn_to_move)
            white_pos = w_r, w_c
    else:
        pawn_to_move = "Black"
        if w_r == b_r + 1 and (w_c == b_c + 1 or w_c == b_c - 1):
            print(f"Game over! Black win, capture on {label_squares(w_c, w_r + 1)}.")
            break
        else:
            b_r = move_pawns(b_r, pawn_to_move)
            black_pos = b_r, b_c

    turn += 1
