ship_width = float(input())
ship_length = float(input())
ship_height = float(input())
average_astronaut_height = float(input())

cabin_volume = 2 * 2 * (average_astronaut_height + 0.40)
ship_volume = ship_height * ship_length * ship_width
astronaut_count = int(ship_volume / cabin_volume)

if 3 <= astronaut_count <= 10:
    print(f"The spacecraft holds {astronaut_count} astronauts.")
elif astronaut_count < 3:
    print("The spacecraft is too small.")
elif astronaut_count > 10:
    print("The spacecraft is too big.")

