def merge(elements, start_index, end_index):
    if start_index < 0:
        start_index = 0
    if end_index >= len(elements):
        end_index = len(elements) - 1
    merged_items = ''.join(elements[start_index:end_index+1])
    elements[start_index:end_index+1] = [merged_items]


def divide(elements, index, partitions):
    if 0 > index >= len(elements):
        return
    item = elements[index]
    divided_partition = []
    partition_length = len(item) // partitions
    for current_item_index in range(partitions):
        if current_item_index != partitions - 1:
            divided_partition.append(item[current_item_index * partition_length:
                                          (current_item_index + 1) * partition_length])
        else:
            divided_partition.append(item[current_item_index * partition_length:])
            elements[index:index + 1] = divided_partition


my_strings = input().split()
command = input().split()

while command[0] != "3:1":

    if command[0] == "merge":
        start_index, end_index = map(int, command[1:])
        merge(my_strings, start_index, end_index)
    elif command[0] == "divide":
        index, partitions = map(int, command[1:])
        divide(my_strings, index, partitions)

    command = input().split()

print(' '.join(my_strings))
