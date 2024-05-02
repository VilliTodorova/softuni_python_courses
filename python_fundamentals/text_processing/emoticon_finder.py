some_text = input()

for index in range(len(some_text)):
    if some_text[index] == ':':
        print(f':{some_text[index + 1]}')
