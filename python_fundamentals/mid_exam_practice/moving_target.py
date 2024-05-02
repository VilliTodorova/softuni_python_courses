def shoot(targets, index, power):
    if 0 <= index < len(targets):
        targets[index] -= power
        if targets[index] <= 0:
            targets.pop(index)
    return targets


def add(targets, index, value):
    if 0 <= index < len(targets):
        targets.insert(index, value)
    else:
        print("Invalid placement!")
    return targets


def strike(targets, index, radius):
    start_range = index - radius
    end_range = index + radius
    if 0 <= start_range < len(targets) and 0 <= end_range < len(targets):
        targets = targets[:start_range] + targets[end_range + 1:]
    else:
        print("Strike missed!")
    return targets


targets = [int(target) for target in input().split()]
command = input().split()

while command[0] != 'End':

    if command[0] == 'Shoot':
        index, power = int(command[1]), int(command[2])
        targets = shoot(targets, index, power)
    elif command[0] == 'Add':
        index, value = int(command[1]), int(command[2])
        targets = add(targets, index, value)
    elif command[0] == 'Strike':
        index, radius = int(command[1]), int(command[2])
        targets = strike(targets, index, radius)

    command = input().split()

targets = list(map(str, targets))
print('|'.join(targets))
