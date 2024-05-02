import re


def is_valid_password(password):
    pattern = r'^([^<>]+)>(\d{3})\|([a-z]{3})\|([A-Z]{3})\|([^<>]{3})<\1$'

    match = re.match(pattern, password)

    if match:
        return f'Password: {match.group(2)}{match.group(3)}{match.group(4)}{match.group(5)}'
    else:
        return 'Try another password!'


num_passwords = int(input())
passwords = [input() for _ in range(num_passwords)]

for password in passwords:
    result = is_valid_password(password)
    print(result)
