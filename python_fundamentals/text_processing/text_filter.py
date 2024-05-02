ban_list = input().split(', ')
your_text = input()

for word in ban_list:
    while word in your_text:
        your_text = your_text.replace(word, '*' * len(word))

print(your_text)
