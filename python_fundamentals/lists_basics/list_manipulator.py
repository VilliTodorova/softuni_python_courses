initial_sequence = input().split()
command = input()

while command != "end":
    manipulator = command.split()
    result = []
    if manipulator[0] == "exchange":
        index = int(manipulator[1])
        if 0 <= index < len(initial_sequence):
            initial_sequence = initial_sequence[index + 1:] + initial_sequence[:index + 1]
        else:
            print("Invalid index")
    print(result)
    command = input()
