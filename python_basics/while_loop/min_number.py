from sys import maxsize

command = input()
min_number = maxsize

while command != "Stop":
    current_number = int(command)
    if current_number < min_number:
        min_number = current_number
    command = input()
print(min_number)
