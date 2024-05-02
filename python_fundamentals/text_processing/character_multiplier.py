def calculate_sum_of_multiplied_codes(str1, str2):
    total_sum = 0

    # Iterate through the characters of both strings
    for char1, char2 in zip(str1, str2):
        # Multiply character codes and add to the total sum
        total_sum += ord(char1) * ord(char2)

    # If one string is longer than the other, add remaining character codes
    if len(str1) > len(str2):
        total_sum += sum(ord(char) for char in str1[len(str2):])
    elif len(str2) > len(str1):
        total_sum += sum(ord(char) for char in str2[len(str1):])

    return total_sum


input_str = input()
str1, str2 = input_str.split()

result = calculate_sum_of_multiplied_codes(str1, str2)
print(result)
