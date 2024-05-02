def min_num(sequence):
    return f'The minimum number is {min(sequence)}'


def max_num(sequence):
    return f'The maximum number is {max(sequence)}'


def sum_nums(sequence):
    return f'The sum number is: {sum(sequence)}'


your_sequence = input().split()
sequence = list(map(int, your_sequence))

print(f'{min_num(sequence)}\n{max_num(sequence)}\n{sum_nums(sequence)}')
