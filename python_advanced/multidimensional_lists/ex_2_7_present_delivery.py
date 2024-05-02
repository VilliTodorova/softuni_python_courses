santa_gifts = int(input())
size = int(input())
da_hood = []
santa_pos = []
nice_kids = 0
visited_nice = 0

directions = {
    "up": (-1, 0),
    "down": (1, 0),
    "left": (0, -1),
    "right": (0, 1),
}


def cookie_monster(gifts_left, good_kids):
    for coords in directions.values():
        r = santa_pos[0] + coords[0]
        c = santa_pos[1] + coords[1]

        if da_hood[r][c].isalpha():
            if da_hood[r][c] == "V":
                good_kids += 1

            da_hood[r][c] = "-"
            gifts_left -= 1

        if not gifts_left:
            break

    return gifts_left, good_kids


for row in range(size):
    da_hood.append(input().split())

    if "S" in da_hood[row]:
        santa_pos = [row, da_hood[row].index("S")]
        da_hood[row][santa_pos[1]] = "-"

    nice_kids += da_hood[row].count("V")

command = input()

while command != "Christmas morning":
    santa_pos = [
        santa_pos[0] + directions[command][0],
        santa_pos[1] + directions[command][1],
    ]

    current_house = da_hood[santa_pos[0]][santa_pos[1]]

    if current_house == "V":
        visited_nice += 1
        santa_gifts -= 1
    elif current_house == "C":
        santa_gifts, visited_nice = cookie_monster(santa_gifts, visited_nice)

    da_hood[santa_pos[0]][santa_pos[1]] = "-"

    if not santa_gifts or nice_kids == visited_nice:
        break

    command = input()

da_hood[santa_pos[0]][santa_pos[1]] = "S"

if not santa_gifts and visited_nice < nice_kids:
    print('Santa ran out of presents!')

print(*[' '.join(line) for line in da_hood], sep='\n')

if nice_kids == visited_nice:
    print(f'Good job, Santa! {visited_nice} happy nice kid/s.')
else:
    print(f'No presents for {nice_kids - visited_nice} nice kid/s.')
