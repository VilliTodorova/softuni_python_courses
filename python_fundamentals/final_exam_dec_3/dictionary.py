def create_dictionary():
    input_string = input()
    word_definitions = input_string.split('|')
    my_dictionary = {}

    for pair in word_definitions:
        word, definition = pair.split(':')
        if word.strip() not in my_dictionary:
            my_dictionary[word.strip()] = []
        my_dictionary[word.strip()].append(definition.strip())

    return my_dictionary


def search_dictionary(my_dictionary):
    words_to_search = input().split('|')
    results = {}

    for word in words_to_search:
        clean_word = word.strip()
        if clean_word in my_dictionary:
            results[clean_word] = my_dictionary[clean_word]

    return results


def print_test_results(search_results):
    for word, definitions in search_results.items():
        print(f"{word}:")
        for definition in definitions:
            print(f" -{definition}")


def print_hand_over_results(dictionary_words):
    for word in dictionary_words:
        print(word, end=" ")


my_dictionary = create_dictionary()

search_results = search_dictionary(my_dictionary)

command = input()

if command == 'Test':
    print_test_results(search_results)
elif command == 'Hand Over':
    print_hand_over_results(my_dictionary.keys())
