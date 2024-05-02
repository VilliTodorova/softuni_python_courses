def loot(chest_state, loot_list):
    index = 0
    for item in loot_list:
        if item not in chest_state:
            chest_state.insert(index, item)

    return chest_state


def drop(chest_state, index):
    if 0 <= index < len(chest_state):
        item = chest_state[index]
        chest_state.pop(index)
        chest_state.append(item)

    return chest_state


def steal(chest_state, count):
    if count >= len(chest_state):
        # If count is greater than or equal to the number of items in the chest, steal all items.
        stolen_items = chest_state
        chest_state = []
    else:
        # Steal the last 'count' items.
        stolen_items = chest_state[-count:]
        chest_state = chest_state[:-count]

    print(', '.join(stolen_items))
    return chest_state


chest_state = input().split('|')
command = input().split()

while command and command[0] != "Yohoho!":  # Check if command is not empty and then the first element

    if command[0] == 'Loot':
        loot_list = command[1:]
        chest_state = loot(chest_state, loot_list)
    elif command[0] == 'Drop':
        index = int(command[1])
        chest_state = drop(chest_state, index)
    elif command[0] == 'Steal':
        count = int(command[1])
        chest_state = steal(chest_state, count)

    command = input().split()

if len(chest_state) <= 0:
    print("Failed treasure hunt.")
else:
    total_length = 0
    for item in chest_state:
        total_length += len(item)
    average_gains = total_length / len(chest_state)
    print(f"Average treasure gain: {average_gains:.2f} pirate credits.")
