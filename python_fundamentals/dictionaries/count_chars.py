symbols = [char for char in input() if char != " "]
unique_letters = {}

for symbol in symbols:
    if symbol not in unique_letters:
        unique_letters[symbol] = 0
    unique_letters[symbol] += 1

for (key, value) in unique_letters.items():
    print(f'{key} -> {value}')
