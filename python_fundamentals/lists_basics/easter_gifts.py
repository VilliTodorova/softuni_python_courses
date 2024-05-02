gift_names = input().split()
command = input().split()

while command[0] != "No" and command[1] != "Money":
    index = 0
    if command[0] == "OutOfStock":
        gift = command[1]
        gift_names = list(map(lambda lack: lack.replace(gift, "None"), gift_names))
    elif command[0] == 'Required':
        index = int(command[2])
        if 0 < index < len(gift_names):
            gift_names[index] = command[1]

    elif command[0] == 'JustInCase':
        gift_names[-1] = command[1]

    command = input().split(' ')

while 'None' in gift_names:
    gift_names.remove('None')

for i in gift_names:
    print(i, end=' ')
