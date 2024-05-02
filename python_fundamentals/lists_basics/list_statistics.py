n = int(input())
list_positives = []
list_negatives = []

for _ in range(n):
    current_integer = int(input())
    if current_integer >= 0:
        list_positives.append(current_integer)
    else:
        list_negatives.append(current_integer)
print(list_positives)
print(list_negatives)
print(f'Count of positives: {len(list_positives)}\n'
      f'Sum of negatives: {sum(list_negatives)}')
