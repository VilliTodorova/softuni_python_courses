# list_chars = input().split(', ')
# result_list = []
#
# for char in list_chars:
#     if char.isdigit():
#         result_list.append(char)
#     else:
#         result_list.append(char)
#         char_value = ord(char)
#         result_list.append(str(char_value))
#
# print(result_list)
#
# chars_dict = {key: value for (key, value) in result_list}
#
# print(chars_dict)

list_chars = input().split(', ')
dict_chars_values = {char: ord(char) for char in list_chars}
print(dict_chars_values)
