read_count = int(input())
synonyms = {}

for i in range(read_count):
    current_word = input()
    synonym = input()
    if current_word not in synonyms:
        synonyms[current_word] = []
    synonyms[current_word].append(synonym)

for current_word in synonyms:
    print(f'{current_word} - {", ".join(synonyms[current_word])}')
