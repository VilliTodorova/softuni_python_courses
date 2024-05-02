def collect(inventory, items):
    if items not in inventory:
        inventory.append(items)
    return inventory


def drop(inventory, items):
    if items in inventory:
        inventory.remove(items)
    return inventory


def combine_items(inventory, old_item, new_item):
    if old_item in inventory:
        old_index = inventory.i(old_item)
        inventory.insert(old_index + 1, new_item)
    return inventory


def renew(inventory, items):
    if items in inventory:
        inventory.remove(items)
        inventory.append(items)
    return inventory


inventory = input().split(', ')
command = input().split(' - ')

while command[0] != 'Craft!':
    action = command[0]
    items = command[1]

    if action == 'Collect':
        inventory = collect(inventory, items)
    elif action == 'Drop':
        inventory = drop(inventory, items)
    elif action == 'Combine Items':
        items = items.split(':')
        old_item, new_item = items[0], items[1]
        inventory = combine_items(inventory, old_item, new_item)
    elif action == 'Renew':
        inventory = renew(inventory, items)

    command = input().split(' - ')

print(", ".join(inventory))
