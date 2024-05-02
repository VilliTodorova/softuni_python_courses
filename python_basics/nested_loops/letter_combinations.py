start = input()
end = input()
skip_letter = input()

count = 0

for i in range(ord(start), ord(end) + 1):
    for j in range(ord(start), ord(end) + 1):
        for k in range(ord(start), ord(end) + 1):
            if chr(i) != skip_letter and chr(j) != skip_letter and chr(k) != skip_letter:
                print(chr(i) + chr(j) + chr(k), end=' ')
                count += 1

print(count)
