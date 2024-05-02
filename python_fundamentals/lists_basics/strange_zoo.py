my_animals_list = []
for _ in range(3):
    body_part = input()
    my_animals_list.append(body_part)

my_animals_list[0], my_animals_list[2] = my_animals_list[2], my_animals_list[0]

print(my_animals_list)
