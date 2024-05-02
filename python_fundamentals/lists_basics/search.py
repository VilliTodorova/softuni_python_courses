n = int(input())
special_word = input()
list_phrases = []

for _ in range(n):
    current_phrase = input()
    list_phrases.append(current_phrase)
print(list_phrases)

for i in range(len(list_phrases) - 1, -1, -1):
    phrase = list_phrases[i]
    if special_word not in phrase:
        list_phrases.remove(phrase)
print(list_phrases)
