from collections import deque


def test_word(char, word):
    if char in word:
        word = word.replace(char, "")
    return word


words = ["rose", "tulip", "lotus", "daffodil"]
words_copy = words.copy()
is_found = False

vowels_sequence = deque(input().split())
consonants_sequence = input().split()

while vowels_sequence and consonants_sequence:
    v = vowels_sequence.popleft()
    c = consonants_sequence.pop()

    for i in range(len(words)):
        words[i] = test_word(v, words[i])

        if words[i] == '':
            is_found = True
            break

        words[i] = test_word(c, words[i])

        if words[i] == '':
            is_found = True
            break
            
    if is_found:
        break

if not is_found:
    print("Cannot find any word!")
else:
    found_index = words.index("")
    print(f"Word found: {words_copy[found_index]}")

if vowels_sequence:
    print(f"Vowels left: {' '.join(vowels_sequence)}")

if consonants_sequence:
    print(f"Consonants left: {' '.join(consonants_sequence)}")
