class NameTooShortError(Exception):
    pass


class MustContainAtSymbolError(Exception):
    pass


class InvalidDomainError(Exception):
    pass


class NameTooLongError(Exception):
    pass


class MustIncludeSpecialCharsError(Exception):
    pass


ACCEPTED_DOMAINS = ("com", "bg", "net", "org")
SPECIAL_CHARS = ('!', '"', '#', '$', '%', '&', "'", '(', ')', '*', '+', ',', '-', '.', '/')


while True:
    email = input("Enter an email address or type 'End' to exit the program: ")

    if email.lower() == "end":
        break

    try:

        if "@" not in email:
            raise MustContainAtSymbolError("Valid email addresses must contain @ symbol!")

        name, domain = email.split("@")

        if len(name) <= 4:
            raise NameTooShortError("Name must be more than 4 characters!")

        elif domain.split(".")[-1] not in ACCEPTED_DOMAINS:
            raise InvalidDomainError(f"Domain must be one of the following: {', '.join('.' + dom for dom in ACCEPTED_DOMAINS)}!")

        elif len(name) > 12:
            raise NameTooLongError("Name should not exceed 12 characters!")

        elif not any(char in SPECIAL_CHARS for char in name):
            raise MustIncludeSpecialCharsError("Name must include at least one special character!")

        print("Email is valid.")

    except(NameTooShortError, NameTooLongError, MustContainAtSymbolError,
           InvalidDomainError, MustIncludeSpecialCharsError) as error:
        print(f"Invalid email: {error}")
