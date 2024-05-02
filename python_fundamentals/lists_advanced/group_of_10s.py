def assign_groups():
    input_sequence = input()
    numbers = [int(num) for num in input_sequence.split(', ')]
    group_boundary = 10

    while numbers:
        group = [num for num in numbers if num <= group_boundary]
        numbers = [num for num in numbers if num > group_boundary]

        print(f"Group of {group_boundary}'s: {group}")

        group_boundary += 10


assign_groups()
