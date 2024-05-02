class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class InvalidLengthError(Exception):
    pass


class InvalidFormatError(Exception):
    pass


class InvalidCharacterError(Exception):
    pass


def validate_email(email):
    name, domain = email.split('@')

    if len(name) <= 4:
        raise NameTooShortError("Name must be more than 4 characters")

    if '@' not in email:
        raise MustContainAtSymbolError("Email must contain @")

    if '.' not in domain:
        raise InvalidDomainError("Domain must contain .")

    valid_domains = ['.com', '.bg', '.net', '.org']
    if not any(domain.endswith(valid_domain) for valid_domain in valid_domains):
        raise InvalidDomainError("Domain must be one of the following: .com, .bg, .org, .net")

    if len(email) > 50:
        raise InvalidLengthError("Email length must be less than or equal to 50 characters")

    if email.count('@') != 1:
        raise InvalidFormatError("Invalid email format")

    invalid_characters = ['!', '#', '$', '%', '&', '*', '+', '/', '=', '?', '^', '`', '{', '|', '}', '~']
    if any(char in email for char in invalid_characters):
        raise InvalidCharacterError("Invalid characters in email")

    print("Email is valid")


while True:
    email = input()
    if email == "End":
        break

    try:
        validate_email(email)
    except (NameTooShortError, MustContainAtSymbolError, InvalidDomainError, InvalidLengthError, InvalidFormatError,
            InvalidCharacterError) as besides:
        print(besides)
