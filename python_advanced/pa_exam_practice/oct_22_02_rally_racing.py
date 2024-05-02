def tunnel_move(command, tunnel_pos):
    r = tunnel_pos[0] + directions[command][0]
    c = tunnel_pos[1] + directions[command][1]

    return [r, c]


size = int(input())
racing_num = int(input())
row, col = [0, 0]

race_route = [input().split() for _ in range(size)]

distance_covered = 0
has_finished = False

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}

command = input()

while command != "End":
    row += directions[command][0]
    col += directions[command][1]

    car_pos = [row, col]

    if race_route[row][col] == "T":
        tunnel_pos = [row, col]
        race_route[row][col] = "."

        for i in range(len(race_route)):
            for j in range(len(race_route[i])):
                if race_route[i][j] == "T":
                    row = i
                    col = j
                    race_route[row][col] = "."
                    car_pos = [row, col]
        # row, col = tunnel_move(command, tunnel_pos)
        # car_pos = [row, col]
        distance_covered += 30
    elif race_route[row][col] == "F":
        car_pos = [row, col]
        distance_covered += 10
        has_finished = True
        print(f"Racing car {racing_num} finished the stage!")
        break
    else:
        car_pos = [row, col]
        distance_covered += 10

    command = input()

race_route[row][col] = "C"

if not has_finished:
    print(f"Racing car {racing_num} DNF.")

print(f"Distance covered {distance_covered} km.")

for i in race_route:
    print("".join(el for el in i))