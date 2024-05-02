start = int(input())
finish = int(input())
magic_number = int(input())
combo_is_found = False
combinations_counter = 0

for x in range(start, finish + 1):
    for y in range(start, finish + 1):
        combinations_counter += 1
        if x + y == magic_number:
            combo_is_found = True
            break
    if combo_is_found:
        break

if combo_is_found:
    print(f"Combination N:{combinations_counter} ({x} + {y} = {magic_number})")
else:
    print(f"{combinations_counter} combinations - neither equals {magic_number}")
