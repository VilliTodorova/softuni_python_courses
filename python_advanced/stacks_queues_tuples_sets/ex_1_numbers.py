first_sequence = set(int(x) for x in input().split())
second_sequence = set(int(x) for x in input().split())

for _ in range(int(input())):
    command_one, command_two, *nums = input().split()
    command = command_one + " " + command_two

    if command == "Add First":
        [first_sequence.add(int(num)) for num in nums]
    elif command == "Add Second":
        [second_sequence.add(int(num)) for num in nums]
    elif command == "Remove First":
        [first_sequence.discard(int(num)) for num in nums]
    elif command == "Remove Second":
        [second_sequence.discard(int(num)) for num in nums]
    else:
        print(first_sequence.issubset(second_sequence) or second_sequence.issubset(first_sequence))

print(*sorted(first_sequence), sep=", ")
print(*sorted(second_sequence), sep=", ")

