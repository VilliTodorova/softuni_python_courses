your_string = input()
digits = ''
letters = ''
others = ''

for char in your_string:
    if char.isdigit():
        digits += char
    elif char.isalpha():
        letters += char
    else:
        others += char

print(f'{digits}\n{letters}\n{others}')
