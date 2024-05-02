guest_list = set(input() for _ in range(int(input())))

command = input()

while command != "END":
    if command in guest_list:
        guest_list.remove(command)
    command = input()

print(len(guest_list))
for code in sorted(guest_list):
    print(code)
