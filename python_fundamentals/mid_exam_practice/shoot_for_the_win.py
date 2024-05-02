targets_value = [int(target) for target in input().split()]
command = input()
shots = 0

while command != "End":
    index = int(command)
    if index >= len(targets_value) or targets_value[index] == -1:
        pass
    else:
        shot_value = targets_value[index]  # Store the value of the target
        targets_value[index] = -1  # Mark the target as shot

        for i in range(len(targets_value)):
            if i != index and targets_value[i] != -1:
                if targets_value[i] > shot_value:
                    targets_value[i] -= shot_value
                elif targets_value[i] <= shot_value:
                    targets_value[i] += shot_value

        shots += 1

    command = input()

targets_value = list(map(str, targets_value))

print(f"Shot targets: {shots} -> " + ' '.join(targets_value))
