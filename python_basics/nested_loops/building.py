floors = int(input())
rooms = int(input())
letter_floors = ""
number_rooms = 0

for floor in range(floors, 0, -1):
    if floor == floors:
        letter_floors = "L"
    elif floor % 2 == 0:
        letter_floors = "O"
    elif floor % 2 != 0:
        letter_floors = "A"
    for room in range(rooms):
        number_rooms = room
        print(f"{letter_floors}{floor}{number_rooms}", end=' ')
    print()
