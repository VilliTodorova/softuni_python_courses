from collections import deque

your_words = deque(input().split())

colors = {"red", "yellow", "blue", "green", "orange", "purple"}

needed_colors = {
    "orange": {"red", "yellow"},
    "purple": {"blue", "red"},
    "green": {"yellow", "blue"},
}

result = []

while your_words:
    first_word = your_words.popleft()
    second_word = your_words.pop() if your_words else ''

    for checked_color in (first_word + second_word, second_word + first_word):
        if checked_color in colors:
            result.append(checked_color)
            break
    else:
        for el in (first_word[:-1], second_word[:-1]):
            if el:
                your_words.insert(len(your_words) // 2, el)

for checked_color in set(needed_colors.keys()).intersection(result):
    if not needed_colors[checked_color].issubset(result):
        result.remove(checked_color)

print(result)
