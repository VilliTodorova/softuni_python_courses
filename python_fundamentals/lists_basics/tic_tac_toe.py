board = [input().split() for _ in range(3)]

player1_won = False
for i in range(3):
    if all(board[i][j] == '1' for j in range(3)):  # Check rows
        player1_won = True
        break
    if all(board[j][i] == '1' for j in range(3)):  # Check columns
        player1_won = True
        break
if all(board[i][i] == '1' for i in range(3)) or all(board[i][2 - i] == '1' for i in range(3)):  # Check diagonals
    player1_won = True

player2_won = False
for i in range(3):
    if all(board[i][j] == '2' for j in range(3)):  # Check rows
        player2_won = True
        break
    if all(board[j][i] == '2' for j in range(3)):  # Check columns
        player2_won = True
        break
if all(board[i][i] == '2' for i in range(3)) or all(board[i][2 - i] == '2' for i in range(3)):  # Check diagonals
    player2_won = True

if player1_won:
    print("First player won")
elif player2_won:
    print("Second player won")
else:
    print("Draw!")
