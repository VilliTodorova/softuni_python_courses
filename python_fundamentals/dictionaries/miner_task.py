mined_dict = {}

while True:
    resource = input()
    if resource == 'stop':
        break
    else:
        quantity = int(input())

    if resource not in mined_dict:
        mined_dict[resource] = 0
    mined_dict[resource] += quantity

for (key, value) in mined_dict.items():
    print(f'{key} -> {value}')
