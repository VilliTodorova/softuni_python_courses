def chars_to_position(a, b):
    start_range = ord(a)
    end_range = ord(b)
    char_list = [chr(i) for i in range(start_range + 1, end_range)]
    result = " ".join(char_list)

    return result


a = input()
b = input()

output = chars_to_position(a, b)
print(output)
