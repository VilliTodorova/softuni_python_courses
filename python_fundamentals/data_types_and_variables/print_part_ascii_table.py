start_char = int(input())
end_char = int(input())
result = ""

for i in range(start_char, end_char + 1):
    print(chr(i), end=' ')
