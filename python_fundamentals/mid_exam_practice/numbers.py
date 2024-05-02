num_sequence = [int(num) for num in input().split()]
average_num = sum(num_sequence) / len(num_sequence)
new_sequence = []

for num in num_sequence:
    if num > average_num:
        new_sequence.append(num)
if len(new_sequence) == 0:
    print('No')
else:
    new_sequence = sorted(new_sequence, reverse=True)

    if len(new_sequence) > 5:
        new_sequence = new_sequence[0:5]
    new_sequence = list(map(str, new_sequence))
    print(' '.join(new_sequence))
