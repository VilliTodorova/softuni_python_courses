width = int(input())
length = int(input())
height = int(input())
command = input()

apartment_volume = width * length * height  # m^3
box_volume = 1  # m^3

boxes_filled = 0

while command != "Done":
    boxes_filled += int(command)
    if boxes_filled >= apartment_volume or command == "Done":
        break
    command = input()

space_left = apartment_volume - boxes_filled

if command == "Done" and space_left > 0:
    print(f"{space_left} Cubic meters left.")
elif space_left < 0:
    print(f"No more free space! You need {abs(space_left)} Cubic meters more.")
