eggs_count = int(input())
red_eggs_count = 0
orange_eggs_count = 0
blue_eggs_count = 0
green_eggs_count = 0
max_dyed = ""
max_eggs = 0

for _ in range(eggs_count):
    dye_colour = input()

    if dye_colour == "red":
        red_eggs_count += 1
        if red_eggs_count > max_eggs:
            max_eggs = red_eggs_count
            max_dyed = "red"
    elif dye_colour == "orange":
        orange_eggs_count += 1
        if orange_eggs_count > max_eggs:
            max_eggs = orange_eggs_count
            max_dyed = "orange"
    elif dye_colour == "blue":
        blue_eggs_count += 1
        if blue_eggs_count > max_eggs:
            max_eggs = blue_eggs_count
            max_dyed = "blue"
    elif dye_colour == "green":
        green_eggs_count += 1
        if green_eggs_count > max_eggs:
            max_eggs = green_eggs_count
            max_dyed = "green"

print(f"Red eggs: {red_eggs_count}\n"
      f"Orange eggs: {orange_eggs_count}\n"
      f"Blue eggs: {blue_eggs_count}\n"
      f"Green eggs: {green_eggs_count}\n"
      f"Max eggs: {max_eggs} -> {max_dyed}")
