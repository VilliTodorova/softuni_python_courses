def round_numbers(numbers):
    """
    Rounds a list of numbers and returns the result as a list.

    Args:
    numbers (list): List of numbers to be rounded.

    Returns:
    list: List of rounded numbers.
    """
    rounded_numbers = [round(float(number)) for number in numbers]
    return rounded_numbers


input_numbers = input().split()
rounded_numbers = round_numbers(input_numbers)

print(rounded_numbers)
