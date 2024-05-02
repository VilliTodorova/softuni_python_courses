detergent_bottles = int(input())
detergent_quantity = detergent_bottles * 750
detergent_is_enough = True
cycles_counter = 0
detergent_used = 0
plates_counter = 0
pots_counter = 0

command = input()

while command != "End" and command != "":
    cycles_counter += 1
    if cycles_counter % 3 != 0:
        plates_counter += int(command)
        detergent_used += 5 * int(command)
    elif cycles_counter % 3 == 0:
        pots_counter += int(command)
        detergent_used += 15 * int(command)
    if detergent_used > detergent_quantity:
        detergent_is_enough = False
        break
    command = input()

detergent_left = detergent_quantity - detergent_used

if detergent_left >= 0:
    print(f"Detergent was enough!\n"
          f"{plates_counter} dishes and {pots_counter} pots were washed.\n"
          f"Leftover detergent {detergent_left} ml.")
elif detergent_left <= 0:
    print(f"Not enough detergent, {abs(detergent_left)} ml. more necessary!")
