some_text = input()
result = ''

for char in some_text:
    char_ascii = ord(char) + 3
    new_char = chr(char_ascii)
    result += new_char

print(result)
