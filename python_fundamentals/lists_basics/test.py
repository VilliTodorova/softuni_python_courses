# Read the initial list
initial_list = list(map(int, input().split()))

while True:
    command = input()
    if command == "end":
        break

    split_command = command.split()
    action = split_command[0]

    if action == "exchange":
        index = int(split_command[1])
        if 0 <= index < len(initial_list):
            initial_list = initial_list[index + 1:] + initial_list[:index + 1]
        else:
            print("Invalid index")
    elif action in ["max", "min"]:
        even = action == "max"
        even_odd = split_command[1]
        elements = [int(x) for x in initial_list if (even and x % 2 == 0) or (not even and x % 2 != 0)]

        if not elements:
            print("No matches")
        else:
            extrema = max(elements) if even_odd == "even" else min(elements)
            extrema_index = len(initial_list) - 1 - initial_list[::-1].index(extrema)
            print(extrema_index)
    elif action in ["first", "last"]:
        count = int(split_command[1])
        even_odd = split_command[2]
        elements = [int(x) for x in initial_list if
                    (even_odd == "even" and x % 2 == 0) or (even_odd == "odd" and x % 2 != 0)]

        if count > len(elements):
            print("Invalid count")
        else:
            sublist = elements[:count] if action == "first" else elements[-count:]
            print(sublist)

print(f"[{', '.join(map(str, initial_list))}]")
