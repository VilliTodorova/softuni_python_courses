def main():
    game_sequence = input().split()
    moves_counter = 0

    while True:
        moves_counter += 1
        command = input()
        # if len(game_sequence) < 0:
        #     break
        if command == 'end':
            print(f"Sorry you lose :(\n{' '.join(game_sequence)}")
            break

        index1, index2 = map(int, command.split())

        if is_invalid_index(index1, index2, game_sequence):
            handle_invalid_input(game_sequence, moves_counter)
        else:
            handle_valid_input(index1, index2, game_sequence, moves_counter)


def is_invalid_index(index1, index2, sequence):
    return(
        index1 == index2
        or index1 < 0
        or index2 < 0
        or index1 >= len(sequence)
        or index2 >= len(sequence)
    )


def handle_invalid_input(sequence, counter):
    middle_index = len(sequence) // 2
    sequence.insert(middle_index, f"-{counter}a")
    sequence.insert(middle_index, f"-{counter}a")
    print('Invalid input! Adding additional elements to the board')


def handle_valid_input(index1, index2, sequence, counter):
    if sequence[index1] == sequence[index2]:
        print(f"Congrats! You have found matching elements - {sequence[index1]}!")
        second_element = sequence[index2]
        sequence.pop(index1)
        sequence.remove(second_element)
    else:
        print("Try again!")

    if len(sequence) == 0:
        print(f"You have won in {counter} turns!")
        exit()


main()
