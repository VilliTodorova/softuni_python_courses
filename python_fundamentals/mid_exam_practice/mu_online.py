def potion(initial_health, health_pack):
    healing_received = min(100 - initial_health, health_pack)
    initial_health += healing_received
    print(f"You healed for {healing_received} hp.")
    print(f"Current health: {initial_health} hp.")
    return initial_health


def chest(initial_bitcoins, found_bitcoins):
    print(f"You found {found_bitcoins} bitcoins.")
    initial_bitcoins += found_bitcoins
    return initial_bitcoins


def monster(initial_health, attack, name):
    initial_health -= attack
    if initial_health > 0:
        print(f"You slayed {name}.")
    else:
        print(f"You died! Killed by {name}.")
    return initial_health


dungeon_rooms = input().split('|')
room_counter = 0
initial_health = 100
initial_bitcoins = 0

for room in dungeon_rooms:
    room_counter += 1
    command = room.split()
    action = command[0]
    amount = int(command[1])

    if action == 'potion':
        initial_health = potion(initial_health, amount)
    elif action == 'chest':
        initial_bitcoins = chest(initial_bitcoins, amount)
    else:
        initial_health = monster(initial_health, amount, action)
        if initial_health <= 0:
            print(f"Best room: {room_counter}")
            break

if initial_health > 0:
    print(f"You've made it!\nBitcoins: {initial_bitcoins}\nHealth: {initial_health}")
