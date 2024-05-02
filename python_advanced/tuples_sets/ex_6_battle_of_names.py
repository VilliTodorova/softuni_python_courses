odd_set = set()
even_set = set()

for row in range(1, int(input()) + 1):
    name = input()
    chars_sum_ind = 0
    for char in name:
        chars_sum_ind += ord(char)
    current_value = int(chars_sum_ind / row)
    if current_value % 2 == 0:
        even_set.add(current_value)
    else:
        odd_set.add(current_value)

if sum(odd_set) == sum(even_set):
    result = list(odd_set.union(even_set))
elif sum(odd_set) > sum(even_set):
    result = list(odd_set.difference(even_set))
else:
    result = list(odd_set.symmetric_difference(even_set))

print(*result, sep=", ")
