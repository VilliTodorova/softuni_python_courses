def tribonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [1]
    elif n == 2:
        return [1, 1]

    sequence = [1, 1, 2]
    while len(sequence) < n:
        next_term = sequence[-1] + sequence[-2] + sequence[-3]
        sequence.append(next_term)

    return sequence


n = int(input())
tribonacci_sequence = tribonacci(n)
result = ' '.join(map(str, tribonacci_sequence))
print(result)
