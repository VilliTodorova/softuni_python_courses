valuables = {'shards': 0, 'fragments': 0, 'motes': 0}
current_items = input().split()
legendary_is_obtained = False
legendary_item = ""

while not legendary_is_obtained:

    for i in range(0, len(current_items), 2):
        key = current_items[i + 1].lower()
        value = int(current_items[i])
        if key not in valuables:
            valuables[key] = 0
        valuables[key] += value

        if valuables['shards'] >= 250:
            legendary_item = 'Shadowmourne'
            valuables['shards'] -= 250
            legendary_is_obtained = True
        elif valuables['fragments'] >= 250:
            legendary_item = 'Valanyr'
            valuables['fragments'] -= 250
            legendary_is_obtained = True
        elif valuables['motes'] >= 250:
            legendary_item = 'Dragonwrath'
            valuables['motes'] -= 250
            legendary_is_obtained = True

        if legendary_is_obtained:
            print(f'{legendary_item} obtained!')
            break

    if legendary_is_obtained:
        break

    current_items = input().split()

for material, quantity in valuables.items():
    print(f'{material}: {quantity}')
    