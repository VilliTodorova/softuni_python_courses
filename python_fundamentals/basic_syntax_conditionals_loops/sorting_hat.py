command = input()
is_voldemort = False

while command != "Welcome!":
    name = command
    if len(name) < 5:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif len(name) > 6:
        if name == "Voldemort":
            is_voldemort = True
            print("You must not speak of that name!")
            break
        print(f"{name} goes to Hufflepuff.")

    command = input()

if not is_voldemort:
    print("Welcome to Hogwarts.")
