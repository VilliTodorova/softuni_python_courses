def calculate_points(dartboard, row, col):
    if row < 0 or col < 0 or row >= len(dartboard) or col >= len(dartboard[0]):
        return 0

    cell = dartboard[row][col]
    if cell.isdigit():
        return int(cell)
    elif cell == "D":
        return 2 * (int(dartboard[row][0]) + int(dartboard[row][-1]) + int(dartboard[0][col]) + int(dartboard[-1][col]))
    elif cell == "T":
        return 3 * (int(dartboard[row][0]) + int(dartboard[row][-1]) + int(dartboard[0][col]) + int(dartboard[-1][col]))
    elif cell == "B":
        return float('inf')  # Bullseye, return positive infinity


# Parse input
first_player, second_player = input().split(", ")
dartboard = [input().split() for _ in range(7)]
throws = []

# Read the throws until the end of input
while True:
    try:
        throw = input()
        if not throw:
            break
        throws.append(throw)
    except EOFError:
        break

# Initialize player scores and turn count
p1_score = p2_score = 501
turn_count = 0

# Play the game
for i, throw in enumerate(throws):
    # Determine current player
    current_player = first_player if i % 2 == 0 else second_player

    # Calculate points for the throw
    row, col = map(int, throw.strip("()").split(", "))
    points = calculate_points(dartboard, row, col)

    # Deduct points from current player's score
    if current_player == first_player:
        p1_score -= points
    else:
        p2_score -= points

    # Check if current player won
    if (current_player == first_player and p1_score <= 0) or (current_player == second_player and p2_score <= 0):
        print(f"{current_player} won the game with {turn_count + 1} throws!")
        break

    # Check if current player hit a bullseye
    if points == float('inf'):
        print(f"{current_player} won the game with {turn_count + 1} throws!")
        break

    # Increment turn count after each pair of throws
    if i % 2 != 0:
        turn_count += 1
