def sort_nums(num_sequence):
    nums_as_int = list(map(int, num_sequence))
    return sorted(nums_as_int)


num_sequence = input().split()
print(sort_nums(num_sequence))

