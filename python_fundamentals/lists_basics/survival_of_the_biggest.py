list_as_string = input().split()
remove_count = int(input())

list_of_integers = [int(x) for x in list_as_string]

for _ in range(remove_count):
    if len(list_of_integers) == 0:
        break
    min_num = min(list_of_integers)
    list_of_integers.remove(min_num)

# Print the remaining numbers
result = ', '.join(map(str, list_of_integers))
print(result)
