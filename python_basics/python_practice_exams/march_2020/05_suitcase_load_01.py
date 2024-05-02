trunk_capacity = float(input())
suitcases_loaded = 0
is_enough = True
suitcases_counter = 0

command = input()
while command != "End":
    suitcase_volume = float(command)

    suitcases_counter += 1
    if suitcases_counter % 3 == 0:
        suitcase_volume *= 1.1

    if suitcase_volume > trunk_capacity:
        print("No more space!")
        is_enough = False
        break
    elif suitcase_volume == trunk_capacity:
        suitcases_loaded += 1
        print("No more space!")
        is_enough = False
        break

    suitcases_loaded += 1
    trunk_capacity -= suitcase_volume
    command = input()

if is_enough and command == "End":
    print("Congratulations! All suitcases are loaded!")

print(f"Statistic: {suitcases_loaded} suitcases loaded.")