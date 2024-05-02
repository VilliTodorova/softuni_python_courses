def words_sorting(*words):
    word_dict = {}

    for word in words:
        word_value = 0

        for char in word:
            word_value += ord(char)

        word_dict[word] = word_value

    if sum(word_dict.values()) % 2 == 0:
        result_even = [f"{key} - {value}" for key, value in sorted(word_dict.items())]
        return f"\n".join(result_even)
    else:
        result_odd = [f"{key} - {value}" for key, value in sorted(word_dict.items(), key=lambda x: -x[1])]
        return f"\n".join(result_odd)


# print(words_sorting(
#         'escape',
#         'charm',
#         'mythology'))

print(
    words_sorting(
        'escape',
        'charm',
        'eye'
  ))
