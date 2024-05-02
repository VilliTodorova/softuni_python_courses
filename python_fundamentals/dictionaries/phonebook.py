phonebook_entries = input()
phonebook_dict = {}
search_range = 0

while True:
    if phonebook_entries.isnumeric():
        search_range = int(phonebook_entries)
        break
    list_entries = phonebook_entries.split('-')
    name, phone_number = list_entries[0], list_entries[1]

    if name not in phonebook_dict:
        phonebook_dict[name] = 0
    phonebook_dict[name] = phone_number

    phonebook_entries = input()

for i in range(search_range):
    searched_name = input()
    if searched_name in phonebook_dict:
        print(f'{searched_name} -> {phonebook_dict[searched_name]}')
    else:
        print(f'Contact {searched_name} does not exist.')
