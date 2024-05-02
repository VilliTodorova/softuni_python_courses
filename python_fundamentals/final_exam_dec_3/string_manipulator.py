def translate(initial_string, char, replacement):
    return initial_string.replace(char, replacement)


def include(initial_string, substring):
    return substring in initial_string


def start(initial_string, substring):
    return initial_string.startswith(substring)


def lowercase(initial_string):
    return initial_string.lower()


def find_index(initial_string, char):
    return initial_string.rfind(char)


def remove(initial_string, start_index, count):
    return initial_string[:start_index] + initial_string[start_index + count:]


initial_string = input()

while True:
    command = input().split()

    if command[0] == 'End':
        break

    if command[0] == 'Translate':
        char, replacement = command[1], command[2]
        initial_string = translate(initial_string, char, replacement)
        print(initial_string)
    elif command[0] == 'Includes':
        substring = command[1]
        print(include(initial_string, substring))
    elif command[0] == 'Start':
        substring = command[1]
        print(start(initial_string, substring))
    elif command[0] == 'Lowercase':
        initial_string = lowercase(initial_string)
        print(initial_string)
    elif command[0] == 'FindIndex':
        char = command[1]
        print(find_index(initial_string, char))
    elif command[0] == 'Remove':
        start_index, count = int(command[1]), int(command[2])
        initial_string = remove(initial_string, start_index, count)
        print(initial_string)
