def add_phone(phones_in_stock, current_phone):
    if current_phone not in phones_in_stock:
        phones_in_stock.append(current_phone)

    return phones_in_stock


def remove_phone(phones_in_stock, current_phone):
    if current_phone in phones_in_stock:
        phones_in_stock.remove(current_phone)

    return phones_in_stock


def bonus_phone(phones_in_stock, old_phone, new_phone):
    if old_phone in phones_in_stock:
        index = phones_in_stock.i(old_phone)
        phones_in_stock.insert(index + 1, new_phone)

    return phones_in_stock


def last_phone(phones_in_stock, current_phone):
    if current_phone in phones_in_stock:
        phones_in_stock.remove(current_phone)
        phones_in_stock.append(current_phone)

    return phones_in_stock


phones_in_stock = input().split(', ')
command = input().split(' - ')

while command[0] != 'End':

    if command[0] == 'Add':
        current_phone = command[1]
        phones_in_stock = add_phone(phones_in_stock, current_phone)
    elif command[0] == 'Remove':
        current_phone = command[1]
        phones_in_stock = remove_phone(phones_in_stock, current_phone)
    elif command[0] == 'Bonus phone':
        new_command = command[1].split(':')
        old_phone, new_phone = new_command[0], new_command[1]
        phones_in_stock = bonus_phone(phones_in_stock, old_phone, new_phone)
    elif command[0] == 'Last':
        current_phone = command[1]
        phones_in_stock = last_phone(phones_in_stock, current_phone)

    command = input().split(' - ')

print(', '.join(phones_in_stock))
