symbols = ("-", ",", ".", "!", "?")

with open("files/text.txt", "r") as even_lines_file:
    text = even_lines_file.readlines()

for r in range(0, len(text), 2):

    for sym in symbols:
        text[r] = text[r].replace(sym, "@")

    print(*text[r].split()[::-1])
    