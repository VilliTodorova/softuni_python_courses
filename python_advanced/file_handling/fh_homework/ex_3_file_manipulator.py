import os

command = input()

while command != "End":
    action, *info = command.split("-")

    if action == "Create":
        with open(f"files/{info[0]}", "w"): pass

    elif action == "Add":
        with open(f"files/{info[0]}", "a") as file:
            file.write(f"{info[1]}\n")

    elif action == "Replace":
        try:
            with open(f"files/{info[0]}", "r+") as file:
                text = file.read()
                text = text.replace(info[1], info[2])

                file.seek(0)
                file.write(text)
                file.truncate()
        except FileNotFoundError:
            print("An error occurred!")

    elif action == "Delete":
        try:
            os.remove(f"files/{info[0]}")
        except FileNotFoundError:
            print("An error occurred!")

    command = input()
