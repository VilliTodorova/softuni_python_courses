size = int(input())
collected_tea = 0
wonderland = []
alice_pos = []

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

for row in range(size):
    wonderland.append(input().split())
    if "A" in wonderland[row]:
        alice_pos = [row, wonderland[row].index("A")]
        wonderland[row][alice_pos[1]] = "*"

while collected_tea < 10:
    dir = input()

    row = alice_pos[0] + directions[dir][0]
    col = alice_pos[1] + directions[dir][1]

    if not (0 <= row < size and 0 <= col < size):
        break

    alice_pos = [row, col]
    current_position = wonderland[row][col]
    wonderland[row][col] = "*"

    if current_position == "R":
        break

    if current_position.isdigit():
        collected_tea += int(current_position)

if collected_tea < 10:
    print("Alice didn'project make it to the tea party.")
else:
    print("She did it! She went to the party.")

print(*[" ".join(row) for row in wonderland], sep="\n")
