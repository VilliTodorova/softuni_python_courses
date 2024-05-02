def check_if_in(first_string, second_string):
    new_string = [element for element in first_string if any(element in item for item in second_string)]
    return new_string


first_string = input().split(', ')
second_string = input().split(', ')

print(check_if_in(first_string, second_string))
