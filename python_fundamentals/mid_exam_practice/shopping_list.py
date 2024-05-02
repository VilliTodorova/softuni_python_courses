def urgent(grocery_list, item):
    if item not in grocery_list:
        grocery_list.insert(0, item)


def unnecessary(grocery_list, item):
    while item in grocery_list:
        grocery_list.remove(item)


def correct(grocery_list, old_item, new_item):
    if old_item not in grocery_list:
        pass
    elif old_item in grocery_list:
        for i in range(len(grocery_list)):
            if grocery_list[i] == old_item:
                grocery_list[i] = new_item


def rearrange(grocery_list, item):
    if item in grocery_list:
        index = grocery_list.i(item)
        grocery_list.pop(index)
        grocery_list.append(item)


grocery_list = input().split('!')
command = input().split()

while command[0] != 'Go':

    if command[0] == 'Urgent':
        item = command[1]
        urgent(grocery_list, item)
    elif command[0] == 'Unnecessary':
        item = command[1]
        unnecessary(grocery_list, item)
    elif command[0] == 'Correct':
        old_item = command[1]
        new_item = command[2]
        correct(grocery_list, old_item, new_item)
    elif command[0] == 'Rearrange':
        item = command[1]
        rearrange(grocery_list, item)

    command = input().split()

print(", ".join(grocery_list))


