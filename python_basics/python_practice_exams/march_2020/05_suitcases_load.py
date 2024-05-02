trunk_capacity = float(input())
suitcases_loaded = 0
command = input()
while command != "End":
    suitcase_volume = float(command)
    if suitcases_loaded > 0 and suitcases_loaded % 3 == 0:
        suitcase_volume *= 1.1
    if suitcase_volume > trunk_capacity:
        print("No more space!")
        break
    else:
        suitcases_loaded += 1
        trunk_capacity -= suitcase_volume
        command = input()
else:
    print("Congratulations! All suitcases are loaded!")
print(f"Statistic: {suitcases_loaded} suitcases loaded.")
