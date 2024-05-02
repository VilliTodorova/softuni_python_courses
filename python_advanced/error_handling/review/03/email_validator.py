import re


class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class MustContainAtLeastOneDigit(Exception):
    pass


class MustNotContainCyrillicCharacters(Exception):
    pass


ALLOWED_DOMAINS = ("com", "bg", "org", "net")
MIN_NAME_LENGTH = 4

line = input()

while line != "End":
    email = line
    email_args = re.split(r"@|\.", email)

    if not email.count("@"):
        raise MustContainAtSymbolError("Email must contain @")

    elif len(email_args[0]) <= MIN_NAME_LENGTH:
        raise NameTooShortError("Name must be more than 4 characters")

    elif email_args[-1] not in ALLOWED_DOMAINS:
        raise InvalidDomainError(f"Domain must be one of the following: "
                                 f"{', '.join('.' + domain for domain in ALLOWED_DOMAINS)}")

    elif not re.findall(r"\d", email_args[0]):
        raise MustContainAtSymbolError("Name must contain at least one digit")

    elif re.findall(r"[А-Яа-я]", email_args[0]):
        raise MustNotContainCyrillicCharacters("Name must not contain any Cyrillic characters")

    print("Email is valid")

    line = input()




