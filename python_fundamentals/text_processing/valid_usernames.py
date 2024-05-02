usernames_list = input().split(', ')
is_valid = True

for username in usernames_list:
    if 3 <= len(username) <= 16:
        is_valid = True
        for char in username:
            if char.isalpha() or char.isdigit() or char == '-' or char == '_':
                continue
            else:
                is_valid = False
                break
    else:
        is_valid = False

    if is_valid:
        print(username)
