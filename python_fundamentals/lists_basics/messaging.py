numbers_sequence = input().split()
text_sequence = input()
message = ""

for num in numbers_sequence:
    index = sum(int(digit) for digit in str(num))
    index %= len(text_sequence)
    message += text_sequence[index]

    text_sequence = text_sequence[:index] + text_sequence[index + 1:]

print(message)
