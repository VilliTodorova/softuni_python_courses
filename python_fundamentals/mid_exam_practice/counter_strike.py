energy = int(input())
wins = 0

command = input()

while True:

    if command == "End of battle":
        print(f"Won battles: {wins}. Energy left: {energy}")
        break

    distance_to_enemy = int(command)

    if energy - distance_to_enemy >= 0:
        wins += 1
    else:
        print(f"Not enough energy! Game ends with {wins} won battles and {energy} energy")
        break

    energy -= distance_to_enemy

    if wins % 3 == 0:
        energy += wins

    command = input()
