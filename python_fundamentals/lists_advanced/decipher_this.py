def decipher_this():
    secret_message = input().split()

    for word in secret_message:
        result = []
        index_of_first_letter = 0
        for i in range(len(word)):

            if not word[i].isdigit():
                index_of_first_letter = i
                break

        # Extract the number as a string
        number_str = word[:index_of_first_letter]

        # Convert the number string to an integer and then to a character
        char_code = int(number_str)
        character = chr(char_code)
        result.append(character)
        # Extract the remaining letters
        remaining_letters = word[index_of_first_letter:]
        if len(remaining_letters) >= 2:
            # Swap the first and last letter
            first_letter = remaining_letters[0]
            last_letter = remaining_letters[-1]
            remaining_letters = last_letter + remaining_letters[1:-1] + first_letter

        result.append(remaining_letters)
        print(''.join(result), end=" ")


decipher_this()
