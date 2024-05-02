
house_height = float(input())
wall_length = float(input())
roof_height = float(input())
WINDOW_AREA = 1.5 * 1.5
DOOR_AREA = 1.2 * 2

green_paint_surface = (wall_length * house_height * 2 - WINDOW_AREA * 2) + ((house_height ** 2) * 2 - DOOR_AREA)
red_paint_surface = (house_height * wall_length * 2) + 2 * (roof_height * house_height / 2)

green_paint = green_paint_surface / 3.4
red_paint = red_paint_surface / 4.3

print('{:.2f}\n{:.2f}'.format(green_paint, red_paint))
