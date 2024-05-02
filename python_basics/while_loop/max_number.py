from sys import maxsize

command = input()
max_number = -maxsize

while command != "Stop":
    current_number = int(command)
    if current_number > max_number:
        max_number = current_number
    command = input()
print(max_number)
