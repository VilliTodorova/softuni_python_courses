while True:
    command = input()

    if command == 'end':
        break

    reverse_word = command[::-1]
    print(f'{command} = {reverse_word}')