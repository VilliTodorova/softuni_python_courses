def check_is_valid_pass(password):
    error_messages = []
    if not (6 <= len(password) <= 10):
        error_messages.append("Password must be between 6 and 10 characters")
    if not password.isalnum():
        error_messages.append("Password must consist only of letters and digits")
    digit_count = sum(1 for char in password if char.isdigit())
    if digit_count < 2:
        error_messages.append("Password must have at least 2 digits")

    if error_messages:
        for message in error_messages:
            print(message)
        return False

    print("Password is valid")
    return True


password = input()
check_is_valid_pass(password)
