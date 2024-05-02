key = int(input())
lines_count = int(input())
result = ""
for i in range(lines_count):
    char = input()
    ascii_code = ord(char)
    new_ascii_code = ascii_code + key
    new_char = chr(new_ascii_code)
    result += new_char

print(result)
