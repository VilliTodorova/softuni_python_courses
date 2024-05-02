from string import punctuation

with open("files/text.txt", "r") as text_file:
    text = text_file.readlines()

result_file = open("files/result_1.txt", "w")

for r in range(len(text)):
    letters, punct = 0, 0

    for sym in text[r]:
        if sym.isalpha():
            letters += 1
        if sym in punctuation:
            punct += 1

    result_file.write(f"Line {r + 1}: {''.join(text[r][:-1])} ({letters})({punct})\n")

result_file.close()


