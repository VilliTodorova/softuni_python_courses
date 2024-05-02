fires = input().split("#")
water = int(input())

effort = 0
fire_counter = 0
put_out_cells = []
can_be_put_out = False

for fire in fires:
    values = fire.split(" = ")
    fire_type = values[0]
    water_level = int(values[1])
    if fire_type == "High" and 81 <= water_level <= 125:
        can_be_put_out = True
    elif fire_type == "Medium" and 51 <= water_level <= 80:
        can_be_put_out = True
    elif fire_type == "Low" and 1 <= water_level <= 50:
        can_be_put_out = True
    else:
        can_be_put_out = False
        continue
    if water >= water_level:
        can_be_put_out = True
    else:
        can_be_put_out = False
        continue

    if can_be_put_out:
        water -= water_level
        effort += water_level * 0.25
        fire_counter += water_level
        put_out_cells.append(water_level)
    else:
        continue

print("Cells:")
for cell in put_out_cells:
    print(f' - {cell}')
print(f"Effort: {effort:.2f}")
print(f"Total Fire: {fire_counter}")
