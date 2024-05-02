your_string = input()
output_string = ""
last_added = ""

for current_char in your_string:
    if current_char != last_added:
        output_string += current_char
        last_added = current_char

print(output_string)
