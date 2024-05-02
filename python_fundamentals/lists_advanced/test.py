def decipher_word(word):
    if word[:-1].isdigit():
        char_code = int(word[:-1])  # Extract the character code as an integer
        first_letter = chr(char_code)  # Convert the character code to a character
        remaining_letters = list(word[1:-1])  # Extract the letters between the first and last letters
        print(first_letter)
        if len(remaining_letters) >= 2:
            # Swap the second and last letters
            remaining_letters[0], remaining_letters[-1] = remaining_letters[-1], remaining_letters[0]

        # Combine the character code, modified letters, and the last letter
        decoded_word = first_letter + ''.join(remaining_letters) + word[-1]
    #     return decoded_word
    # else:
    #     return word


# Example usage
word1 = "72olle"
word2 = "103doo"
decoded_word1 = decipher_word(word1)
decoded_word2 = decipher_word(word2)
# print(decoded_word1)  # Output: "Hello"
# print(decoded_word2)  # Output: "Good"
decipher_word(word1)